mkpip
=====

Boilerplate python packaging

Tools
-----

:mkpip: Creates boilerplate python module
:mkbin: Creates a boilerplate script with argparse args, options and flags
:bumpy: Bumps the version in all recursive files in a python module (``__version__`` stuff)

mkpip
-----
	usage: mkpip [-h] [--keywords KEYWORDS] [--dest DEST] [--config CONFIG]
				 [--author AUTHOR] [--email EMAIL] [--year YEAR]
				 [--copyright-holder COPYRIGHT_HOLDER]
				 [--license-path LICENSE_PATH] [--license LICENSE] [--url URL]
				 name desc

	positional arguments:
	  name                  Name of project.
	  desc                  Description of project. Will go in README.rst,
							setup.py, and license

	optional arguments:
	  -h, --help            show this help message and exit
	  --keywords KEYWORDS, -k KEYWORDS
							keywords in setup.py
	  --dest DEST, -d DEST  Destination directory that contains project folder
							(default ./$name)
	  --config CONFIG, -c CONFIG
							Name of config key in ~/.mkpip.cfg
	  --author AUTHOR, -a AUTHOR
							Author
	  --email EMAIL, -e EMAIL
							Author's email
	  --year YEAR, -y YEAR  copyright year
	  --copyright-holder COPYRIGHT_HOLDER, -C COPYRIGHT_HOLDER
							copyright holder
	  --license-path LICENSE_PATH, --lp LICENSE_PATH
							custom license template path
	  --license LICENSE, -l LICENSE
							license in setup.py
	  --url URL, -r URL     url pattern for project's repo

mkbin
-----

	usage: mkbin [-h] [--flags FLAGS] [--pos POS] [--opts OPTS] [--output OUTPUT]
				 [--boto] [--collections] [--flask] [--mysqldb] [--psycopg2]
				 [--requests] [--standard] [--subprocess] [--yamlcfg]

	optional arguments:
	  -h, --help            show this help message and exit
	  --flags FLAGS, -F FLAGS
							name of flags
	  --pos POS, -P POS     name of positionals
	  --opts OPTS, -O OPTS  name of optionals
	  --output OUTPUT, --out OUTPUT, -o OUTPUT
							output script path
	  --boto, -b            add boto connection import statements
	  --collections, --coll, -c
							add collections, namedtuple and defaultdict
	  --flask, --fl, -f     add flask import and boilerplate
	  --mysqldb, --mysql, -m
							add mysqldb import
	  --psycopg2, --psql, -p
							add psycopg2 imports
	  --requests, --req, -r
							add requests import statement
	  --standard, --std, -s
							add os,sys imports
	  --subprocess, --sub, -S
							add subprocess imports
	  --yamlcfg, --ycfg, -y
							add yamlcfg imports

bumpy
-----

	usage: bumpy [-h] [--check] [--major] [--minor] [--patch] [--set SET]
				 [--root-dir ROOT_DIR] [--push] [--quiet] [--dry]

	optional arguments:
	  -h, --help            show this help message and exit
	  --check, -c           print current version
	  --major, -M           bump major
	  --minor, -m           bump minor
	  --patch, -p           bump patch level
	  --set SET, -s SET     set version number
	  --root-dir ROOT_DIR, -r ROOT_DIR
							path to root directory with files with versions
	  --push, -P            tag and push using git
	  --quiet, -q
	  --dry, -d

releases
--------

:0.9.3: fix MANIFEST
:0.9.2: Changed config to be solely ``~/.mkpip.cfg`` and allow you to specify values under [default] and [other], then -c other uses that.
:0.9.1: Add ``--include-paths``/``-i`` option to restrict to few files
:0.9.0: Fixed bumpy to find all ``__version__`` stuff as well when bumping
:0.8.3: Fixed .gitignore template
:0.8.2: Added stuff like ``__title__`` and ``__author__`` to the ``__init__.py``
:0.8.1: Deleted extra whitespace in ``__init__.py``
:0.8.0: - Refactored mkpip with some major improvements
        - checks configs from .py, .yml and .cfg
        - uses {format} notation instead of %(this)s
        - added tox files for easy test generation
