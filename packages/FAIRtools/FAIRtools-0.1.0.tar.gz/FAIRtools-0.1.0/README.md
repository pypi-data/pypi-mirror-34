# Python Package for FAIR Evaluator Client
[![Build Status](https://travis-ci.com/c-martinez/FAIR_Evaluator_Client.svg?branch=master)](https://travis-ci.com/c-martinez/FAIR_Evaluator_Client)
- TODO:
  - configure travis to test builds from wilkinsonlab
  - change travis badge to show status of builds from wilkinsonlab

Python client to the FAIR Metrics Evaluator REST interface

## What this package does?
TODO

## How to install the package
Install via `pip`:

```
pip install git+https://github.com/wilkinsonlab/FAIR_Evaluator_Client.git
```

 - TODO: add to [PyPI](https://pypi.org/)

## Usage example
```python
from FAIRtools import Collections
from FAIRtools import Metrics
from FAIRtools import Evaluations

id = ''
c = Collections(id)
c.title()
```

## Documentation
* Documentation can be found in the `docs` folder.

## Testing and code coverage

* Tests are in the `tests` folder.
* The testing framework used is [PyTest](https://pytest.org). For more information on PyTest see [their introduction](http://pythontesting.net/framework/pytest/pytest-introduction/).
* Tests can be run with `python setup.py test`
  - This is configured in `setup.py` and `setup.cfg`
* [Travis CI](https://travis-ci.com/) is used to run tests automatically.
  - Configuration can be found in `.travis.yml`

## Software citation
Mario Prieto Godoy, Carlos Martinez, & Mark Wilkinson. (2018, July 19). wilkinsonlab/FAIR_Evaluator_Client: First FAIR Evaluator Client release (Version v0.1.0). Zenodo. http://doi.org/10.5281/zenodo.1315447 .

# License
Copyright (c) 2018, Wilkinson Laboratory for Biological Informatics

MIT license
