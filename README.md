[![GitHub top language](https://img.shields.io/github/languages/top/FHPythonUtils/PyGraudit.svg?style=for-the-badge)](../../)
[![Codacy grade](https://img.shields.io/codacy/grade/[codacy-proj-id].svg?style=for-the-badge)](https://www.codacy.com/manual|gh/FHPythonUtils/PyGraudit)
[![Repository size](https://img.shields.io/github/repo-size/FHPythonUtils/PyGraudit.svg?style=for-the-badge)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/PyGraudit.svg?style=for-the-badge)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/PyGraudit.svg?style=for-the-badge)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/PyGraudit.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/PyGraudit.svg?style=for-the-badge)](../../commits/master)


<!-- omit in toc -->
# PyGraudit

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">


PyGraudit uses graudit signature sets that allows you to find potential
security flaws in source code. It's comparable to
other static analysis applications like RATS, SWAAT and flaw-finder while
keeping the technical requirements to a minimum and being very flexible.


- [Install With PIP](#install-with-pip)
- [Usage](#usage)
- [Databases](#databases)
- [Credits](#credits)
- [Community Files](#community-files)
	- [Licence](#licence)
	- [Changelog](#changelog)
	- [Code of Conduct](#code-of-conduct)
	- [Contributing](#contributing)
	- [Security](#security)
	- [Support](#support)
	- [Rationale](#rationale)


## Install With PIP

```python
pip install pygraudit
```

Head to https://pypi.org/project/pygraudit/ for more info


## Usage

PyGraudit supports several options and tries to follow good shell practices. For
a list of the options you can run pygraudit -h or see below. The simplest way to
use PyGraudit is;

```none
usage: __main__.py [-h] [--format FORMAT] [--db DB] [-B] [-A] [-z] [-Z] [-l] [--file FILE] path_to_scan

Python version of graudit by Wireghoul https://github.com/wireghoul/graudit

Formats
- ansi (for terminal)
- json
- markdown
- csv

positional arguments:
  path_to_scan          Path to scan (.) for current directory

optional arguments:
  -h, --help            show this help message and exit
  --format FORMAT, -f FORMAT
                        Output format. One of ansi, json, markdown, csv. default=ansi
  --db DB, -d DB        db to use. One of {DB_FILES}, default=python
  -B                    Suppress banner
  -A                    Scan ALL files
  -z                    Suppress colours
  -Z                    High contrast colours
  -l                    Lists databases available
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
