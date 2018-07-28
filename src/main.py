import crossosgit
import sys
from pathlib import Path

class Main:
    def start(self, args):
        try:
            configFile = Path(args[0]).expanduser().resolve()
        except:
            print('Could not find the config file.')
        xosgit = crossosgit.CrossOsGit(configFile)
        xosgit.update()

main = Main()
main.start(sys.argv[1:])
