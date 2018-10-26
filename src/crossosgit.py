import git
import repogroup
from pathlib import Path

class CrossOsGit:
    def __init__(self, configFile: Path):
        self.group = self.loadRepoGroup(configFile)

    def update(self):
        for repo in self.group.repos:
            path = self.group.destinationDir / repo.name
            if path.exists():
                self.pull(repo)
            else:
                self.clone(repo)

    def clone(self, repo: repogroup.GitRepo):
        destinationPath = self.group.destinationDir / repo.name
        print('Cloning {} to {}'.format(repo.url, destinationPath))
        git.Repo.clone_from(str(repo.url), str(destinationPath))

    def pull(self, repo: repogroup.GitRepo):
        print('Pulling {}'.format(repo))
        path = self.group.destinationDir / repo.name
        repo = git.Repo(path)
        origin = repo.remotes.origin
        origin.pull()

    def loadRepoGroup(self, configFile):
        return repogroup.RepoGroup(configFile)
