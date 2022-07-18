import datetime
import sys
import os
from typing import Optional


try:
    import click
except ImportError:
    print('Installing `click` package, required to run this script.')
    os.system('pip install -U click')
    import click  # noqa

try:
    import github3  # noqa
except ImportError as import_exc:
    print('Installing `github3` package, required to run this script.')
    os.system('pip install -U github3.py')
    import github3  # noqa


def publish_release(*, owner: str, repository_name: str, token: str, tag: str) -> None:
    github = github3.login(token=token)
    repository = github.repository(owner, repository_name)

    try:
        [pull_request] = list(repository.pull_requests(head=f"{owner}:release-{tag}"))
    except ValueError as exc:
        raise RuntimeError(
            f'There should be exactly one pull request for {owner}:release-{tag}'
        ) from exc

    pull_request = repository.pull_request(pull_request.number)

    try:
        [*_, commit] = pull_request.commits()
    except ValueError as exc:
        raise RuntimeError(
            f'There should be at least one commit associated with #{pull_request.number}'
        ) from exc

    try:
        [release] = [release for release in repository.releases() if release.draft]
    except ValueError as e:
        raise RuntimeError('There should be exactly one draft release.') from e

    if commit.status().state != 'success':
        raise RuntimeError(f'checks for #{pull_request.number} have failed')

    if pull_request.is_merged():
        raise RuntimeError(f"#{pull_request.number} has been merged already")

    if not pull_request.mergeable:
        raise RuntimeError(f'#{pull_request.number} is not mergeable')

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
@click.option(
    '--owner',
    metavar='USER',
    required=True,
    envvar='GITHUB_USER',
    help='GitHub username',
)
@click.option(
    '--repository',
    metavar='REPO',
    required=True,
    envvar='GITHUB_REPOSITORY',
    help='GitHub repository',
)
@click.option(
    '--token',
    metavar='TOKEN',
    required=True,
    envvar='GITHUB_TOKEN',
    help='GitHub API token',
)
@click.argument("tag", required=False)
def main(owner: str, repository: str, token: str, tag: Optional[str]) -> None:
    """Publish a GitHub release for this project.

    If you specify no release tag, function uses YYYY.MM.DD with the current
    date.
    There must be a single release draft, and a pull request for a
    branch `release-TAG`. This script merges the pull request and publishes
    the release, taking the release notes from the pull request description.
    """
    if tag is None:
        today = datetime.date.today()
        tag = f'{today:%Y.%-m.%-d}'

    try:
        publish_release(
            owner=owner,
            repository_name=repository,
            token=token,
            tag=tag,
        )
    except Exception as error:
        click.secho(f'Error: {error}', fg='red')
        sys.exit(1)


if __name__ == '__main__':
    main(prog_name='publish-github-release')
