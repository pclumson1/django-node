Django Node
===========

Bindings and utils for integrating Node.js and NPM into a Django application.

```python
from django_node import node, npm

node.run('/path/to/some/file.js', '--some-argument')

npm.install('/path/to/some/directory')
```


Install
-------

```bash
pip install django-node
```


Node.js
-------

The `django_node.node` module provides utils for introspecting and invoking Node.js.

### django_node.node.is_installed

A boolean indicating if Node.js is installed.

### django_node.node.version

A tuple containing the version of Node.js installed. For example, `(0, 10, 33)`

### django_node.node.version_raw

A string containing the raw version returned from Node.js. For example, `'v0.10.33'`

### django_node.node.ensure_installed()

A method which will raise an exception if Node.js is not installed.

### django_node.node.ensure_version_gte()

A method which will raise an exception if the installed version of Node.js is
less than the version required.

Arguments:

`version_required`: a tuple containing the minimum version required.

```python
from django_node import node

node_version_required = (0, 10, 0)

node.ensure_version_gte(node_version_required)
```

### django_node.node.run()

A method which will invoke Node.js with the arguments provided and return the resulting stderr and stdout.

```python
from django_node import node

stderr, stdout = node.run('/path/to/some/file.js', '--some-argument')
```


NPM
---

The `django_node.npm` module provides utils for introspecting and invoking NPM.

### django_node.npm.is_installed

A boolean indicating if NPM is installed.

### django_node.npm.version

A tuple containing the version of NPM installed. For example, `(2, 0, 0)`

### django_node.npm.version_raw

A string containing the raw version returned from NPM. For example, `'2.0.0'`

### django_node.npm.ensure_installed()

A method which will raise an exception if NPM is not installed.

### django_node.npm.ensure_version_gte()

A method which will raise an exception if the installed version of NPM is
less than the version required.

Arguments:

- `version_required`: a tuple containing the minimum version required.

```python
from django_node import npm

npm_version_required = (2, 0, 0)

npm.ensure_version_gte(npm_version_required)
```

### django_node.npm.install()

A method that will invoke `npm install` in a specified directory. Optional arguments will be
appended to the invoked command.

Arguments:

- `target_dir`: a string pointing to the directory which the command will be invoked in.
- `arguments`: an optional tuple of strings to append to the invoked command.
- `silent`: an optional boolean indicating that NPM's output should not be printed to the terminal.

```python
from django_node import npm

# Install the dependencies in a particular directory
stderr, stdout = npm.install('/path/to/some/directory/')

# Install a dependency into a particular directory and persist it to the package.json file
stderr, stdout = npm.install('/path/to/some/directory/', ('--save', 'some-package'))
```

### django_node.npm.run()

A method which will invoke NPM with the arguments provided and return the resulting stderr and stdout.

```python
from django_node import npm

stderr, stdout = npm.run('install', '--save', 'some-package')
```


Settings
--------

### DJANGO_NODE['PATH_TO_NODE']

An path that will resolve to Node.js.

Default:
```python
'node'
```

### DJANGO_NODE['NODE_VERSION_COMMAND']

The command invoked on Node.js to retrieve its version.

Default:
```python
'--version'
```

### DJANGO_NODE['NODE_VERSION_FILTER']

A function which will generate a tuple of version numbers from
the raw version string returned from Node.js.

Default
```python
lambda version: tuple(map(int, (version[1:] if version[0] == 'v' else version).split('.')))
```

### DJANGO_NODE['PATH_TO_NPM']

An path that will resolve to NPM.

Default
```python
'npm'
```

### DJANGO_NODE['NPM_VERSION_COMMAND']

The command invoked on NPM to retrieve its version.

Default
```python
'--version'
```

### DJANGO_NODE['NPM_VERSION_FILTER']

A function which will generate a tuple of version numbers from
the raw version string returned from NPM.

Default
```python
lambda version: tuple(map(int, version.split('.'))),
```

### DJANGO_NODE['NPM_INSTALL_COMMAND']

The install command invoked on NPM. This is prepended to all calls to `django_node.npm.install`.

Default
```python
'install'
```

### DJANGO_NODE['RAISE_ON_MISSING_DEPENDENCIES']

Allow calls to `django_node.node.ensure_installed` and `django_node.npm.ensure_installed`
to raise exceptions if the dependency is not installed.

Default
```python
True
```

### DJANGO_NODE['RAISE_ON_OUTDATED_DEPENDENCIES']

Allow calls to `django_node.node.ensure_version_gte` and `django_node.npm.ensure_version_gte`
to raise exceptions if the dependency is less than the one specified.

Default
```python
True
```


Running the tests
-----------------

```bash
python django_node/tests/runner.py
```