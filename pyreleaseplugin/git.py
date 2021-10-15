from subprocess import Popen, PIPE


def is_tree_clean():
    """
    Check if git working tree is clean.

    Returns:
        False if there are uncommited changes, True otherwise
    """
    # pylint: disable=simplifiable-if-expression
    return False if Popen(["git", "diff-files", "--quiet"]).wait() else True


def get_default_branch():
    """
    Find the default branch of the remote repo.

    Returns:
        branch (str): The default branch
    """
    remote_info = Popen(["git", "remote", "show", "origin"], stdout=PIPE)
    info_sliced = Popen(["awk", "/HEAD branch/ {print $NF}"], stdin=remote_info.stdout, stdout=PIPE)
    head_branch = info_sliced.communicate()[0]
    return head_branch.decode("utf-8").rstrip()


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


def push_code(branch):
    """
    Push code changes to git branch `branch`.
    """
    code = Popen(["git", "push", "origin", branch]).wait()
    if code:
        raise RuntimeError("Error pushing changes to git")


def push_tags():
    """
    Push tags to git.
    """
    code = Popen(["git", "push", "--tags"]).wait()
    if code:
        raise RuntimeError("Error pushing tags to git")


def push(release_branch):
    """
    Push commits and tags to Github.
    """
    push_code(release_branch)
    push_tags()
