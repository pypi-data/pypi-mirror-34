# Version Bumper for Foliant Projects

This CLI extension adds `bump` command that lets you bump Foliant project [semantic version](https://semver.org/) without editing the config manually.


## Installation

```shell
$ pip install foliantcontrib.bump
```


## Usage

Bump version from "1.0.0" to "1.0.1":

```shell
$ foliant bump
Version bumped from 1.0.0 to 1.0.1.
```

Bump major version:

```shell
$ foliant bump -v major
Version bumped from 1.0.1 to 2.0.0.
```

To see all available options, run `foliant bump --help`:

```shell
$ foliant bump --help
usage: foliant bump [-h] [-v VERSION_PART] [-p PATH] [-c CONFIG]

Bump Foliant project version.

optional arguments:
  -h, --help            show this help message and exit
  -v VERSION_PART, --version-part VERSION_PART
                        Part of the version to bump: major, minor, patch, prerelease, or build (default: patch).
  -p PATH, --path PATH  Path to the directory with the config file (default: ".").
  -c CONFIG, --config CONFIG
                        Name of the config file (default: "foliant.yml").
```
