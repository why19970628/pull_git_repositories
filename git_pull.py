from re import I
from time import sleep, time
import git
from git import *
import threading
import os


def isGitDir(dir):
    repdir = os.path.join(os.path.abspath('.'), dir)
    repgitdir = os.path.join(repdir, '.git')
    if not os.path.exists(repgitdir):
        return False
    return True


def updateSub(subdir):
    repdir = os.path.join(os.path.abspath('.'), subdir)
    try:
        repo = git.Repo(repdir)
        if repo.is_dirty():
            dirSubDir.append(subdir)
            return
        remote = repo.remote()
        print("start pulling from remote for: %s\r\n" % subdir)
        remote.pull()
        print("Done pulling for %s\r\n" % subdir)
    except NoSuchPathError as e:
        pass
    except InvalidGitRepositoryError as e:
        pass
    finally:
        pass


def get_all_git_dirs():
    currDir = os.path.abspath('.')
    subDirs = []
    for root, dirs, files in os.walk(currDir):
        for dir in dirs:
            p = os.path.join(root, dir)
            if isGitDir(p):
                subDirs.append(p)
    return subDirs


if __name__ == '__main__':
    subDirs = get_all_git_dirs()
    print("ready to update git repo:", subDirs)
    for dir in subDirs:
        print(dir + '\r\n')
    dirSubDir = []
    poole = []

    for subdir in subDirs:
        try:
            updateSub(subdir)
            sleep(5)
        except Exception as e:
            print(e)
    print('dirSubDir \n', dirSubDir)
