Cross OS git
=============
Some scripts to automatically manage loads of git repos.

Config
-------
An example of a config that clones a bunch of vim repositories

_my-config-file.json_
```
{
    "destination-dir": "~/.vim/bundle/",
    "base-url": "https://github.com/",
    "plugins": [
        "tpope/vim-pathogen",
        "tpope/vim-surround",
        "tpope/vim-repeat"
    ]
}
```

Install
--------
Run `pip install gitpython` to load the git GitPython dependency.
Run `python3 xosgit/src/main.py my-config-file.json` to run the tool
