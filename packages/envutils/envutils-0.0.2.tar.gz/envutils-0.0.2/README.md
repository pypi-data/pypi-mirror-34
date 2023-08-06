envutils
--------

This python library contains some utils functions to read and parse environment variables.

It can be installed with:
```bash
pip3 install envutils
```

Usage examples:

```python
# Set some example values for demonstration purposes
>>> import os
>>> os.environ['MY_ENV'] = 'my_value'
>>> os.environ['MY_INT_ENV'] = '42'
>>> os.environ['MY_BOOL_ENV'] = 'True'

>>> from envutils import envutils

# Read env variable as string
>>> envutils.get_from_environment('MY_ENV', 'my_default_value')
'my_value'

# Read env variable as int
>>> envutils.get_int_from_environment('MY_INT_ENV', 666)
42

# Read env variable as boolean
>>> envutils.get_bool_from_environment('MY_BOOL_ENV', False)
True

# Read a non-existing env variable
>>> envutils.get_from_environment('UNSET_ENV', 'my_default_value')
'my_default_value'
```