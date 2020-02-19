# testing client
A testing framework that supports staged and hierarchical testing.

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
```
$ pipenv run python tester/app.py -h     
usage: app.py [-h] [-t TYPE] [-l LEVEL]

Testing client.

optional arguments:
  -h, --help            show this help message and exit
  -t TYPE, --type TYPE  testing type.
  -l LEVEL, --level LEVEL
                        testing level.
```

## Contributing
[Rain Wu](https://github.com/RainrainWu)