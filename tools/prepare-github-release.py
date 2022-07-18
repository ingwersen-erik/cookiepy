"""
Prepare GitHub repository.
"""
from __future__ import annotations, absolute_import
import datetime
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable, List, Optional

import click

try:
    import github3
except ImportError as import_exc:
    import os
    os.system('pip install -U github3.py')
    import github3


def git(*args: str, **kwargs: Any) -> str:
    """Run a git command.

    Parameters
    ----------
    args : str
        String arguments to pass to git command.
        For example, `['commit', '--message', 'message']`.
    kwargs : Any
        Keyword arguments to pass to `subprocess.run`.
        These are arguments that need a value.
        For example, `check=True` for `git commit` command.

    Returns
    -------
    str
        The output of the git command.

    Raises
    ------
    subprocess.CalledProcessError
        If the git command fails to get a successful exit code.
    """
    try:
        process = subprocess.run(
            ["git", *args], check=True, capture_output=True, text=True
        )
        return process.stdout
    except subprocess.CalledProcessError as error:
        print(error.stdout, end="")
        print(error.stderr, end="", file=sys.stderr)
        raise


def replace_text(path: Path | str, old: str, new: str):
    """Replace text in a file.

    Parameters
    ----------
    path : Path | str
        The filepath of the file to change.
    old : str
        Original text.
    new : str
        New text.
    """
    path = Path(path) if isinstance(path, str) else path
    text = path.read_text(encoding='utf-8')
    text = text.replace(old, new)
    path.write_text(text)


def prepare_release(
    *,
    owner: str,
    repository_name: str,
    token: str,
    tag: str,
    remote: str,
    base: str,
    bump_paths: List[Path],
    label_names: List[str],
) -> None:
    """Prepare a GitHub release.

    Parameters
    ----------
    owner : str
        The owner of the GitHub repository.
        For example, `"ingwersen-erik"`.
    repository_name : str
        The name of the GitHub repository.
    token : str
        The GitHub token. You need a token to access a GitHub repo.
        GitHub doesn't authenticate you with you account password anymore.
    tag : str
        The tag to create a GitHub release for.
        For example, `"v0.1.0"`.
    remote : str
        The name of the remote to push to.
        For example, `"origin"`.
    base : str
        The base branch to push to. For example, `"main"`.
    bump_paths : List[Path]
        The filepaths of the files to bump.
        Bump changes the version number in files that specify the
        version number. Common files that might need bumping include:
        `README.rst`, `docs/guide.rst`, `docs/index.rst`, and `docs/quickstart.rst`.
    label_names : List[str]
        The names of the labels to add to the GitHub release.

    Raises
    ------
    ValueError
        If the function fails to generate a valid release.
    RuntimeError
        If you pass an wrong label name.
        Please note that other errors might occur, and that fot using this function,
        you need to have a good understanding of the correct values you need to pass
        to it.

    Notes
    -----
    The `*` argument to this function ignores any positional arguments
    aside from the ones it expects.
    """
    branch = f'release-{tag}'
    title = f'Release {tag}'
    oldtag = git('describe', '--tags', '--abbrev=0').strip()

    git('switch', f'--create={branch}', base)

    for path in bump_paths:
        replace_text(path, oldtag, tag)
        git('add', str(path))

    git('commit', f'--message={title}')
    git('push', '--set-upstream', remote, branch)

    click.echo(f'pushed {branch}')

    github = github3.login(token=token)
    repository = github.repository(owner, repository_name)

    try:
        [release] = [release for release in repository.releases() if release.draft]
    except ValueError as exc:
        raise RuntimeError('There should be exactly one draft release') from exc

    pull_request = repository.create_pull(
        title=title,
        base=base,
        head=f'{owner}:{branch}',
        body=release.body,
    )

    click.echo(f'opened #{pull_request.number}')

    pull_request = repository.pull_request(pull_request.number)
    labels = pull_request.issue().add_labels(*label_names)

    for name in label_names:
        if name not in {label.name for label in labels}:
            raise RuntimeError(f'label {name} missing from #{pull_request.number}')

    click.echo(f'added labels {", ".join(label_names)} to #{pull_request.number}')


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
    "--token",
    metavar="TOKEN",
    required=True,
    envvar="GITHUB_TOKEN",
    help="GitHub API token",
)
@click.option(
    "--remote",
    metavar="REMOTE",
    default="origin",
    help="remote for GitHub repository",
)
@click.option(
    "--base",
    metavar="BRANCH",
    default="main",
    help="default branch of the GitHub repository",
)
@click.option(
    "--bump",
    metavar="FILE",
    multiple=True,
    help="bump the version in these files (may be specified multiple times)",
)
@click.option(
    "labels",
    "--label",
    metavar="LABEL",
    multiple=True,
    help="labels for the pull request (may be specified multiple times)",
)
@click.argument("tag", required=False)
def main(
    owner: str,
    repository: str,
    token: str,
    remote: str,
    base: str,
    bump: Iterable[str],
    labels: Iterable[str],
    tag: Optional[str],
) -> None:
    """Open pull request to release project.

    If no release tag specified, it uses YYYY.MM.DD, with current date.
    There must be a single draft release. This script pushes a branch
    `release-TAG` and opens a pull request for it taking the pull request
    description from the draft release notes. The branch has a single
    commit which updates the version number in the documentation.
    """
    if tag is None:
        today = datetime.date.today()
        tag = f"{today:%Y.%-m.%-d}"

    try:
        prepare_release(
            owner=owner,
            repository_name=repository,
            token=token,
            remote=remote,
            base=base,
            bump_paths=[Path(path) for path in bump],
            label_names=list(labels),
            tag=tag,
        )
    except Exception as error:
        click.secho(f"error: {error}", fg="red")
        sys.exit(1)


if __name__ == "__main__":
    main(prog_name='prepare-github-release')
