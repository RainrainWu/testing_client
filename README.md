# testing client
A testing framework for non-unit-testing, supports group-oriented and hierarchical testing.

## Getting Started
### Prerequisites
- Python 3.7.3

### Running Development
```
pipenv --python 3.7.3
pipenv install --dev
export PYTHONPATH=$PYTHONPATH:$PWD
pipenv run python tester/app.py -t func
```

### Usage
1. Quick help with `-h` flag
```
$ pipenv run python tester/app.py -h     
usage: app.py [-h] [-g GROUP] [-l LEVEL]

Testing client.

optional arguments:
  -h, --help            show this help message and exit
  -g GROUP, --group GROUP
                        testing group.
  -l LEVEL, --level LEVEL
                        testing level.
```

2. Customize your own testing groups `TEST_GROUPS` in *tester/config.py*, default is:
```
TEST_GROUPS = {'func', 'regr'}
```

3. Customize your own testing levels `TEST_LEVELS` from low to high in *tester/config.py*, default is:
```
TEST_LEVELS = ['less', 'common', 'verbose']
```

4. Add the decorator with group and level params to your test case funcion, you can refer to the examples inside *tester/case/example.py*
```python
@mount('func', 'common')
def foo():
    Reporter.header3('test case foo start')
    assert True
    Reporter.header3('test case foo complete')
```

5. Run scripts with group and level flags
```
$ pipenv run python tester/app.py -g func -l common
```

## Contributing
[Rain Wu](https://github.com/RainrainWu)