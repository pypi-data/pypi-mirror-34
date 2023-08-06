Timestamp
=========

# Install
In order to install, you can either use pypi with either
```bash
pip3 install timestamps
```
or
```bash
python3 -m pip install timestamps
```

# Usage
The library has several types defined

# Timestamp
Represents a timestamp with a 10^-7 precision (same as the time.time() of python 3)
You can instanciate it in various ways, each time, you can provide a non-keyword value
	or a value with as keyword either _float, _hex or _datetime
```python

# With a float
t = Timestamp(1.0)
t = Timestamp(_float=1.0)

# With a datetime
t = Timestamp(datetime.datetime.now())
t = Timestamp(_datetime=datetime.datetime.now())

# With an hex
t = Timestamp(_hex='f')
t = Timestamp('0xf0')
t = Timestamp('#FF')
```
