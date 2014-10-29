# Team NewHeaven Website

Team NewHeaven website is the official website of the french minecraft team
NewHeaven. 

You can see the running version [here](http://www.teamnewheaven.fr).

## Language convention

The team is french and user-interface strings are in french but localization is
available. The website is translation into english.

All comments in the code and bug reports must be in english (or french in the
worst scenario).


As for other style matters in the code, the [PEP-8 Style
Guide](http://www.python.org/dev/peps/pep-0008/) is a good base.

## Dependencies

The website uses [Django](https://www.djangoproject.com/), a web framework for
the [Python](http://python.org/) programming language in version 3.

### Basic dependencies (system-dependent)

You should install Python 3, and the
[pip](http://www.pip-installer.org/en/latest/) package manager. See your 
distribution documentation for more informations.

### Virtual python environment (virtualenv)

The `virtualenv` tool is designed to avoid problem with incompatible Python
versions or conflicting package requirements between distinct projects. It
allows to set up per-project local environments, setting a preferred version of
Python, and installing dependencies locally. To install `virtualenv`, simply
run

    :::console
    $ pip install --user virtualenv

For utilisation see the [Official documentation](http://www.virtualenv.org/) or 
[this tutorial](http://sametmax.com/les-environnement-virtuels-python-virtualen
v-et-virtualenvwrapper/) in french.


All the python dependencies for website are listed in the file `requirements.txt`
in the source repository. From the PDP directory, simply run

    :::console
    (venv)$ pip install -r requirements.txt

(This will install the full Django framework and a few separate modules, so it
may take some time.)
