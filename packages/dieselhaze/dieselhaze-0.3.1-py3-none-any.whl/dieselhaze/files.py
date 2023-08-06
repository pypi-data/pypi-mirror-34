import os
import shutil
import stat


def copyfile(src, dst, overwrite=False):
    if overwrite:
        shutil.copy2(src, dst)
        return

    # Open the file and raise an exception if it exists
    fd = os.open(dst, os.O_CREAT | os.O_EXCL | os.O_WRONLY)

    # Copy the file and automatically close files at the end
    with os.fdopen(fd) as f:
        with open(src) as sf:
            shutil.copyfileobj(sf, f)


def copytree(src, dst, symlinks=False, ignore=None):
    """Like shutil.copytree but merge directories."""
    if not os.path.exists(dst):
        os.makedirs(dst)
        shutil.copystat(src, dst)

    lst = os.listdir(src)

    if ignore:
        excl = ignore(src, lst)
        lst = [x for x in lst if x not in excl]

    for item in lst:
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if symlinks and os.path.islink(s):
            if os.path.lexists(d):
                os.remove(d)
            os.symlink(os.readlink(s), d)
            try:
                st = os.lstat(s)
                mode = stat.S_IMODE(st.st_mode)
                os.lchmod(d, mode)
            except:  # noqa
                pass  # lchmod not available
        elif os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            copyfile(s, d)
