# Place Python Package

A python package for interfacing with the Place API

## Installation

To install from GitHub using [pip](http://www.pip-installer.org/en/latest/):

```bash
pip install git+https://github.com/placepay/place-python.git
```

If you don't have pip, it can be installed using the below command:

```bash
curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
```

To manually install `place-python`, you can [download the source](https://github.com/placepay/place-python/zipball/master) and run:

```bash
python setup.py install
```

## Basic usage

```python
import place

# set your api key
place.api_key = 'private_key_6fsMi3GDxXg1XXSluNx1sLEd'

# create an account
account = place.Account.create(
    email='joe.schmoe@example.com',
    full_name='Joe Schmoe',
    user_type='payer'
)
```

## Documentation
Read the [docs](https://developer.placepay.com/?python)
