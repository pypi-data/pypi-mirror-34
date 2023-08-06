from setuptools import setup

setup(
    name="rs3clans",
    description='A Python 3 module wrapper for RuneScape 3 Clan\'s API',
    long_description='''# rs3clans.py
A Python 3 module wrapper for RuneScape 3 Clan's API

Current Version: 0.4.0

***

## Setup:

```bash
python3 -m pip install rs3clans
```

***

### Usage:

* Import:

```python3
import rs3clans
```

- I remade the whole thing so i will need to remake those docs some time. Until then read comments on source code.
```
    ''',
    long_description_content_type='text/markdown',
    version='0.4.0',
    author='John Victor',
    author_email='johnvictorfs@gmail.com',
    license='MIT',
    packages=['rs3clans'],
    zip_safe=False,
    url='https://github.com/johnvictorfs/rs3clans.py',
    classifiers = (
        "Programming Language :: Python :: 3"
    )
)
