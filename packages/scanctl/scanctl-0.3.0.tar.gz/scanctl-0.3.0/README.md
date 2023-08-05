scanctl
=======

> A tool to facilitate managing Whitesource data

![PyPi](https://img.shields.io/pypi/v/scanctl.svg)
![Travis](https://img.shields.io/travis/spotify/scanctl.svg)

### Requirements:

* Python 3.6
* Whitesource [Filesystem Agent][]

[Filesystem Agent]: https://whitesource.atlassian.net/wiki/spaces/WD/pages/33718339/File+System+Agent

### Development:

```sh
$ git clone git@spotify.com:spotify/scanctl.git
$ cd scanctl

# optionally create a virtualenv before installing
$ pyenv virtualenv 3.6.2 venv
$ pyenv activate venv

(venv) $ pip install -r requirements.txt
(venv) $ pip install -e .

# list all organizations and repositories from a remote
(venv) $ scanctl github --token $GITHUB_API_TOKEN list-orgs
(venv) $ scanctl github --token $GITHUB_API_TOKEN list-repos

# run a scan against a particular repository
(venv) $ scanctl scan --token $WHITESOURCE_API_TOKEN spotify/scanctl
```

### Code of Conduct

This project adheres to the [Open Code of Conduct][code-of-conduct]. By
participating, you are expected to honor this code.

[code-of-conduct]: https://github.com/spotify/code-of-conduct/blob/master/code-of-conduct.md
