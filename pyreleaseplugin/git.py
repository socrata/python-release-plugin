from subprocess import Popen


def is_tree_clean():
    """
    Check if git working tree is clean.

    Returns:
        False if there are uncommited changes, True otherwise
    """
    return False if Popen(["git", "diff-files", "--quiet"]).wait() else True


def commit_changes(version):
    """
    Commit current release changes.

    Args:
        version (str): The version specifier to include in the commit message
    """
    commit_message = "Update version file and changlog for release {}".format(version)
    code = Popen(["git", "commit", "-a", "-m", commit_message]).wait()
    if code:
        raise RuntimeError("Error committing changes")


def tag(version):
    """
    Add a tag to the release.

    Args:
        version (str): The version specifier to include in the commit message
    """
    tag = 'v' + version
    code = Popen(["git", "tag", tag]).wait()
    if code:
        raise RuntimeError("Error tagging release")


def push_code(release_branch):
    """
    Push code changes to git branch `release_branch`.
    """
    code = Popen(["git", "push", "origin", release_branch]).wait()
    if code:
        raise RuntimeError("Error pushing changes to git")


def push_tags():
    """
    Push tags to git.
    """
    code = Popen(["git", "push", "--tags"]).wait()
    if code:
        raise RuntimeError("Error pushing tags to git")


def push():
    """
    Push the release commits to Github.
    """
    push_code()
    push_tags()
