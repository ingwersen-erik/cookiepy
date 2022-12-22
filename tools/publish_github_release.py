"""Script allows automatic publish of new project releases on GitHub."""
import datetime
import sys
from typing import Optional
from urllib.error import HTTPError

from prepare_github_release import click, github3


def publish_release(*, owner: str, repository_name: str, token: str,
                    tag: str) -> None:
    """Publish a release on GitHub."""
    github = github3.login(token=token)
    repository = github.repository(owner, repository_name)
    try:
        [pull_request] = list(
            repository.pull_requests(head=f"{owner}:release-{tag}"))
    except ValueError as error:
        raise RuntimeError(
            f'There should be exactly one pull request for {owner}:release-'
            f'{tag}'
        ) from error
    pull_request = repository.pull_request(pull_request.number)

    try:
        [*_, commit] = pull_request.commits()
    except ValueError as error:
        raise RuntimeError(
            'At least one commit needs to be associated with the '
            f'pull request #{pull_request.number} to publish a new release.'
        ) from error

    try:
        [release] = [release for release in repository.releases() if
                     release.draft]
    except ValueError as error:
        raise RuntimeError(
            'There should be exactly one draft release.') from error

    if commit.status().state != 'success':
        raise RuntimeError(f'checks for #{pull_request.number} have failed')

    if pull_request.is_merged():
        raise RuntimeError(f"#{pull_request.number} has been merged already")

    if not pull_request.mergeable:
        raise RuntimeError(f'#{pull_request.number} is not merge-able')

    title = f'{pull_request.title} (#{pull_request.number})'

    if not pull_request.merge(commit_title=title, merge_method='squash'):
        raise RuntimeError(f'Cannot merge #{pull_request.number}')

    pull_request.refresh()

    if not pull_request.is_merged():
        raise RuntimeError(f"#{pull_request.number} was not merged")

    click.echo(f'Merged #{pull_request.number}')
    branch = repository.ref(f'heads/{pull_request.head.ref}')

    if not branch.delete():
        raise RuntimeError(f'Cannot remove {branch.ref}')
    click.echo(f'Removed {branch.ref}')

    if not release.edit(
        tag_name=tag,
        name=tag,
        body=pull_request.body,
        draft=False,
        prerelease=False,
    ):
        raise RuntimeError(f'Cannot publish {release.name}')
    click.echo(f'Published {release.name}')


@click.command()
@click.option('--owner', metavar='USER', required=True, envvar='GITHUB_USER',
              help='GitHub username')
@click.option('--repository', metavar='REPO', required=True,
              envvar='GITHUB_REPOSITORY', help='GitHub repository')
@click.option('--token', metavar='TOKEN', required=True, envvar='GITHUB_TOKEN',
              help='GitHub API token')
@click.argument("tag", required=False)
def main(owner: str, repository: str, token: str, tag: Optional[str]) -> None:
    """
    Publish a GitHub release for this project.

    If no release tag is specified, function uses 'YYYY.MM.DD' with the current
    date as tag. There must be a single release draft, and a pull request for a
    branch `release-TAG`. This script merges the pull request and publishes
    the release, taking the release notes from the pull request description.
    """
    if tag is None:
        tag = f'{datetime.date.today():%Y.%-m.%-d}'
    try:
        publish_release(owner=owner, repository_name=repository,
                        token=token, tag=tag)
    except (HTTPError, ValueError) as error:
        # Handle HTTPError and ValueError
        click.secho(f'Error: {error}', fg='red')
        sys.exit(1)


if __name__ == '__main__':
    main()  # pylint: disable=no-value-for-parameter
