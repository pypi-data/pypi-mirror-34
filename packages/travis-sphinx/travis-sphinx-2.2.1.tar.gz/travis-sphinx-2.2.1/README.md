[![Build Status](https://travis-ci.org/Syntaf/travis-sphinx.svg?branch=master)](https://travis-ci.org/Syntaf/travis-sphinx)
[![codecov](https://codecov.io/gh/Syntaf/travis-sphinx/branch/master/graph/badge.svg)](https://codecov.io/gh/Syntaf/travis-sphinx)

travis-sphinx
=============
A standalone script for automated building and deploying of sphinx docs via travis-ci

#### What does it do? 

travis-sphinx aims to take the hassle out of building and pushing docs to your gh-pages. deploying to your github page can be tedious especially when you're making many small changes overtime or even just making a minor revision you'd like to see live; `travis-sphinx` will automate your build and deploy process with the help of [travis-ci](https://travis-ci.org/)! 

* [Installation](#installation)
* [Getting Started](#getting-started)
  * [Obtaining a personal access token](#obtaining-a-personal-access-token)
  * [Calling travis-sphinx](#calling-travis-sphinx)
  * [Custom repository deployment](#specifying-a-custom-deploy-repository)
* [Example](#example-configuration)
* [Help](#help)

*Check out [cadquery](https://github.com/dcowden/cadquery) for a live example of `travis-sphinx` in action!*

Installation
==============
```
pip install --user travis-sphinx
export PATH=$HOME/.local/bin:$PATH
```

Getting Started
======
If you aren't already familiar with travis-ci, take a look at their [getting-started guide](http://docs.travis-ci.com/user/getting-started/). Otherwise the steps below will outline how to get travis-sphinx running in your repository

The first step you'll need to do is simply make sure you have a gh-pages branch that exists, if it doesn't:
```
git checkout -b gh-pages
git rm -rf .
git push --set-upstream origin gh-pages
```

#### Obtaining a Personal Access Token

travis-sphinx requires a *personal access token* to be able to push changes to `gh-pages`, so you'll need to generate a token to use. Head over to your github account settings:

![img](http://i.imgur.com/eKN3YFl.png)

To generate a token: go to *personal access tokens* and click *generate new token*. Make sure to copy this to your clipboard for the next step!

![img](http://i.imgur.com/yDZRDhI.png)

The easiest way to set this token is to head over to https://travis-ci.org/ and click on *settings* for the repository you'll be using travis-sphinx with. You can add the token by specifying it in the enviroment variable under the name `GH_TOKEN`. You can also follow [this](http://www.hoverbear.org/2015/03/07/rust-travis-github-pages/#givingtravispermissions) tutorial on giving travis permissions, but the first options is much more simple

![img](http://i.stack.imgur.com/J2U27.png)

Now travis-sphinx can push to your gh-pages, all done! The next step is calling travis-sphinx within your `.travis.yml`

#### Calling travis-sphinx
Once your personal access token is setup, you can begin using travis-sphinx within your configuration file. The two calls that should be used are:
```
script:
    - travis-sphinx build
    
after_success:
    - travis-sphinx deploy
```
*build* will generate the actual documentation files while *deploy* will move those files to gh-pages. If you don't have your documentation in the standard `docs/source` path, you can specify **where** they are with `--source`. This tool also assumes that you would like to build and deploy the *master* branch and any *tags* pushed. If you would like to point the tool elsewhere, this can be solved using `--branches` , e.g. `travis-sphinx --branches=test,production` will build and deploy on **only** the test and production branches.
```
script:
    - travis-sphinx build --source=other/dir/doc
    
after_success:
    - travis-sphinx deploy
```

#### Specifying a Custom Deploy Repository

Per [#38](https://github.com/Syntaf/travis-sphinx/pull/38), you can now specify a custom deployment repository if you're using a fork for working on documentation. To do so, under your travis environment variables, using the following constant:

```
GH_REPO_SLUG = 'syntaf/fork-of-my-repo'
```

### Example Configuration

**note:** See this repositories `.travis.yml` for a simpler configuration script. The below script is for conda environments which have a number of dependencies that also need to be installed.

```
language: python - "2.7"

# before_install will simply setup a conda enviroment for installing python packages, if you
# have project dependencies it's usually recommended to go this route
before_install:
    - wget http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh -O miniconda.sh
    - chmod +x miniconda.sh
    - "./miniconda.sh -b"
    - export PATH=/home/travis/miniconda2/bin:$PATH
    - conda update --yes conda
    - sudo rm -rf /dev/shm
    - sudo ln -s /run/shm /dev/shm

install:
    - conda install --yes python="2.7" sphinx
    - pip install --user travis-sphinx

script:
    - travis-sphinx build

after_success:
    - travis-sphinx deploy
```

Also see a working example at the [dnppy](https://github.com/NASA-DEVELOP/dnppy) repository

### Help
```
Usage: travis-sphinx [OPTIONS] COMMAND [ARGS]...

Options:
  --version               Show the version and exit.
  -v, --verbose
  -o, --outdir DIRECTORY  Directory to put html docs, default is target
                          [default: doc/build]
  --help                  Show this message and exit.

Commands:
  build   Build sphinx documentation.
  deploy  Deploy sphinx docs to gh_pages branch by...


Usage: travis-sphinx build [OPTIONS]

  Build sphinx documentation.

Options:
  -s, --source DIRECTORY  Source directory of sphinx docs  [default:
                          doc/source]
  -n, --nowarn BOOLEAN    Do not error on warnings
  --help                  Show this message and exit.


Usage: travis-sphinx deploy [OPTIONS]

  Deploy sphinx docs to gh_pages branch by pulling from output dir.

Options:
  -b, --branches TEXT     Comma separated list of branches to build on
                          [default: master]
  -c, --cname TEXT        Write a CNAME file with the given CNAME.
  -m, --message TEXT      The commit message to use on the target branch.
                          [default: Update documentation]
  -x, --deploy-host TEXT  Specify a custom domain for GitHub, useful for
                          enterprise domains.  [default: github.com]
  --help                  Show this message and exit.
```
