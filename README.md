[![CircleCI](https://circleci.com/gh/ylathouris/bio.svg?style=shield)](https://circleci.com/gh/ylathouris/moet)  ![Coverage](coverage.svg)

---

# Moet

Moet is a programming exercise for the **Water Overflow Problem**.


![Problem]

<br/>

* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Running The Tests](#testing)
* [Starting A Shell](#moet.shell)
* [Command Line Interface (CLI)](#moet.cli)
* [Application Programming Interface (API)](#moet.api)

<br/>


### <a name="prerequisites"></a>Prerequisites

Before getting started, there are a few things you will need. These
are as follows:

* An internet connection
* [git] installed on your machine (used to clone the source code)
* [tox] installed on your machine (used to run the tests)
* Python 3.5 or higher installed on your machine

<br/>


### <a name="installation"></a>Installation

This package has not been published to a public repository. The best 
way to install it is to clone the source code directly.

```bash
$ git clone https://github.com/ylathouris/moet
$ cd moet
```

Once you're in the root directory of the moet repository you can run 
the installer script. This will create a virtual environment and install 
moet's dependencies into that environment.

```bash
$ ./install.sh
``` 

<br/>



### <a name="testing"></a>Running The Tests

If you're looking for documentation on how the code works, the tests 
are the best place to start. This project uses [tox], as well as 
[pytest] and [hypothesis], to run and manage the tests. To execute 
the tests, simply run the following command from the package root: 

```bash
$ tox
```

<br/>

### <a name="moet.shell"></a>Starting A Shell

To start using the `moet` command (CLI), or the API from a Python 
interpreter, you'll first need to setup a suitable environment. There
is a bootstrap to help with this. Simply run the following command
from the package root:

```bash
$ source .venv/bin/activate
``` 

All this does is put you inside the virtual environment that was 
created during the installation process. To get out of the shell, 
run 

```bash
deactivate
```


<br/>

### <a name="moet.cli"></a>Command Line Interface (CLI)

Once you're in a suitable environment. You should have access to the 
`moet` command. There some example commands in this section but you 
can also run:

```bash
$ moet --help
```

<br/>

**Running with the defaults (no arguments)**

This builds a tower of glasses with 4 rows and pours 3.75 litres of 
liquid into the top most glass. This should be enough liquid to 
completely fill each glass in the tower. 

```bash
$ moet
```


<br/>

**Specify the amount of liquid**

You can specify the amount of liquid to pour into the top most glass
by using the `--fill` option. For example: 

```bash
$ moet --fill 2.5
```


<br/>

**Highlight a glass**

You can highlight a specific glass in the tower to get information 
about the amount of liquid in that glass. There are two ways to do 
this:

**1.** Provide the glass ID using the `--uid` option:
 

```bash
$ moet --fill 2.5 --uid=E
```

**2.** Provide the position of the glass (i.e. i and j) using the 
`--position` option:
 

```bash
$ moet --fill 2.5 --position 2 1
```


<br/>

**Show breakdown**

You can show a breakdown of the liquid in each glass using the 
`--breakdown` option. For example:

```bash
$ moet --fill 3.75 --position 4 0 --breakdown
```

<br/>

### <a name="moet.api"></a>Application Programming Interface (API)

There is also a Python API you can use. Here is an example:

```python
import moet

# Create a tower with 4 rows of glasses. 
tower = moet.create_tower(rows=4)

# Get the rows in the tower.
rows = tower.get_rows()

# Iterate over the rows:
for glasses in rows:
    for glass in glasses:
        print(">", glass.uid, glass.position, glass.quantity)

# Get a specific glass.
glass = tower.get_glass("E")

# Get the parents for that glass.
parents = tower.get_parents(glass)

# Get the children for that glass.
children = tower.get_children(glass)
```  


[Problem]: docs/images/problem.png
[git]: https://git-scm.com/
[pipenv]: https://pipenv.readthedocs.io/en/latest/basics/
[tox]: https://tox.readthedocs.io/en/latest/
[pytest]: https://docs.pytest.org/en/latest/
[hypothesis]: https://hypothesis.readthedocs.io/en/latest/index.html