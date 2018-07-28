import json
from pathlib import Path, PurePath

class RepoGroup:
    def __init__(self, configFile: Path):
        self.destinationDir = ''
        self.repos = []

        self.load(configFile)

    def load(self, configFile: Path):
        jsonFile = self.loadJson(configFile)

        self.destinationDir = Path(val(jsonFile, 'destination-dir')).expanduser().resolve()
        baseUrl = valOr(jsonFile, 'base-url', 'https://github.com/')
        repoUrls = val(jsonFile, 'plugins')

        self.repos = [GitRepo(baseUrl, r) for r in repoUrls]

    def loadJson(self, path):
        try:
            with open(path, 'r') as fd:
                return json.load(fd)
        except:
            print('Could not open or parse the json file (' + path + ').')
            return None


class GitRepo:
    def __init__(self, baseUrl: str, repoUrl: str):
        self.url = baseUrl + '/' + repoUrl
        self.name = PurePath(self.url).name

    def __str__(self):
        return self.name


def val(content, key):
    try:
        return content[key]
    except (TypeError, KeyError):
        return None

def valOr(content, key, alternative):
    value = val(content, key)
    return alternative if value == None or value == '' or value == [] else value
