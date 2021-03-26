====================== No Longer Supported (Soon) =====================

**This project has reached the end of development and will be no longer
supported once removed from `simplesecurity`**

========================= No Longer Supported =========================

**This project has reached the end of development and is no longer
supported**

## What this means now
- The repository, issues, pull requests, labels, milestones, projects, wiki,
releases, commits, tags, branches, reactions and comments are read-only.
- The repository can still be forked and cloned - The License still applies.

## What this means in the future
- The repository is scheduled for deletion (the earliest date for this is
01/08/2021)
- The repository may be un-archived (however, this is very unlikely)

========================= No Longer Supported =========================


[![GitHub top language](https://img.shields.io/github/languages/top/FHPythonUtils/PyGraudit.svg?style=for-the-badge)](../../)
[![Repository size](https://img.shields.io/github/repo-size/FHPythonUtils/PyGraudit.svg?style=for-the-badge)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/PyGraudit.svg?style=for-the-badge)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/PyGraudit.svg?style=for-the-badge)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/PyGraudit.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/PyGraudit.svg?style=for-the-badge)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/pygraudit.svg?style=for-the-badge)](https://pypistats.org/packages/pygraudit)
[![PyPI Total Downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=total%20downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fpygraudit)](https://pepy.tech/project/pygraudit)
[![PyPI Version](https://img.shields.io/pypi/v/pygraudit.svg?style=for-the-badge)](https://pypi.org/project/pygraudit)

<!-- omit in toc -->
# PyGraudit

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">

Python version of graudit by Wireghoul https://github.com/wireghoul/graudit

PyGraudit uses graudit signature sets that allows you to find potential
security flaws in source code. It's comparable to
other static analysis applications like RATS, SWAAT and flaw-finder while
keeping the technical requirements to a minimum and being very flexible.


- [Usage](#usage)
- [Databases](#databases)
- [Credits](#credits)
- [Documentation](#documentation)
- [Install With PIP](#install-with-pip)
- [Language information](#language-information)
	- [Built for](#built-for)
- [Install Python on Windows](#install-python-on-windows)
	- [Chocolatey](#chocolatey)
	- [Download](#download)
- [Install Python on Linux](#install-python-on-linux)
	- [Apt](#apt)
- [How to run](#how-to-run)
	- [With VSCode](#with-vscode)
	- [From the Terminal](#from-the-terminal)
- [Download Project](#download-project)
	- [Clone](#clone)
		- [Using The Command Line](#using-the-command-line)
		- [Using GitHub Desktop](#using-github-desktop)
	- [Download Zip File](#download-zip-file)
- [Community Files](#community-files)
	- [Licence](#licence)
	- [Changelog](#changelog)
	- [Code of Conduct](#code-of-conduct)
	- [Contributing](#contributing)
	- [Security](#security)
	- [Support](#support)
	- [Rationale](#rationale)


## Usage

PyGraudit supports several options and tries to follow good shell practices. For
a list of the options you can run pygraudit -h or see below. The simplest way to
use PyGraudit is;

```none
usage: __main__.py [-h] [--format FORMAT] [--db DB] [-B] [-A] [-z] [-Z] [-l] [--exclude EXCLUDE [EXCLUDE ...]] [--file FILE]
                   path_to_scan

Python version of graudit by Wireghoul https://github.com/wireghoul/graudit

positional arguments:
  path_to_scan          Path to scan (.) for current directory

optional arguments:
  -h, --help            show this help message and exit
  --format FORMAT, -f FORMAT
                        Output format. One of ansi, json, markdown, csv. default=ansi
  --db DB, -d DB        db to use. One of ['actionscript', 'android', 'asp', 'c', 'cobol', 'default', 'dotnet', 'exec', 'fruit',
'go', 'ios', 'java', 'js', 'nim', 'perl', 'php', 'python', 'ruby', 'secrets-b64', 'secrets', 'spsqli', 'sql', 'strings', 'xss'].
Default=python
  -B                    Suppress banner
  -A                    Scan ALL files
  -z                    Suppress colours
  -Z                    High contrast colours
  -l                    Lists databases available
  --exclude EXCLUDE [EXCLUDE ...], -x EXCLUDE [EXCLUDE ...]
                        Paths to ignore
  --file FILE, -o FILE  Filename to write to (omit for stdout)
```

## Databases

graudit uses extended regular expressions (POSIX) as it's signatures and comes
with several databases ready for use. You can extend the existing databases or
make your own if you require additional signatures.


A list of the database files in order of precedence is shown with the -l switch:
`graudit -l`

The following databases are included:
  - actionscript
  - android
  - asp
  - c
  - cobol
  - default
  - dotnet
  - exec
  - fruit
  - go
  - ios
  - java
  - js
  - perl
  - php
  - python (used if -d argument is omitted)
  - nim
  - ruby
  - secrets
  - spsqli
  - sql
  - strings
  - xss

## Credits

  - Wireghoul - http://www.justanotherhacker.com
  - Various others - see Changelog

## Documentation
See the [Docs](/DOCS/) for more information.

## Install With PIP
```python
pip install pygraudit
```

Head to https://pypi.org/project/pygraudit/ for more info

## Language information
### Built for
This program has been written for Python 3 and has been tested with
Python version 3.9.0 <https://www.python.org/downloads/release/python-380/>.

## Install Python on Windows
### Chocolatey
```powershell
choco install python
```
### Download
To install Python, go to <https://www.python.org/> and download the latest
version.

## Install Python on Linux
### Apt
```bash
sudo apt install python3.9
```

## How to run
### With VSCode
1. Open the .py file in vscode
2. Ensure a python 3.9 interpreter is selected (Ctrl+Shift+P > Python:Select
Interpreter > Python 3.9)
3. Run by pressing Ctrl+F5 (if you are prompted to install any modules, accept)
### From the Terminal
```bash
./[file].py
```

## Download Project
### Clone
#### Using The Command Line
1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to
clone to
4. Type 'git clone' followed by URL in step 2
```bash
$ git clone https://github.com/FHPythonUtils/PyGraudit
```

More information can be found at
<https://help.github.com/en/articles/cloning-a-repository>

#### Using GitHub Desktop
1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
<https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop>

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location

## Community Files
### Licence
MIT & GPLv3 License
(See the [LICENSE](/LICENSE.md) for more information.)

### Changelog
See the [Changelog](/CHANGELOG.md) for more information.

### Code of Conduct
Online communities include people from many backgrounds. The *Project*
contributors are committed to providing a friendly, safe and welcoming
environment for all. Please see the
[Code of Conduct](https://github.com/FHPythonUtils/.github/blob/master/CODE_OF_CONDUCT.md)
 for more information.

### Contributing
Contributions are welcome, please see the
[Contributing Guidelines](https://github.com/FHPythonUtils/.github/blob/master/CONTRIBUTING.md)
for more information.

### Security
Thank you for improving the security of the project, please see the
[Security Policy](https://github.com/FHPythonUtils/.github/blob/master/SECURITY.md)
for more information.

### Support
Thank you for using this project, I hope it is of use to you. Please be aware that
those involved with the project often do so for fun along with other commitments
(such as work, family, etc). Please see the
[Support Policy](https://github.com/FHPythonUtils/.github/blob/master/SUPPORT.md)
for more information.

### Rationale
The rationale acts as a guide to various processes regarding projects such as
the versioning scheme and the programming styles used. Please see the
[Rationale](https://github.com/FHPythonUtils/.github/blob/master/RATIONALE.md)
for more information.
