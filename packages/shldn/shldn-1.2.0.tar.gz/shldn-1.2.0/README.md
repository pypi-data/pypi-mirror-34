# shldn 
Sheldon Cooper ALWAYS points out what (he thinks) is wrong with people and their work

## What is it?

`shldn` is a console-application that finds all the division operations in Python source code to facilitate transitioning Python 2 code to Python 3. It uses Python's [AST](https://docs.python.org/3/library/ast.html) module to process and parse the code. It, then traverses the abstract syntax tree to find all the division operations, and prints them in a normal or more readable format to the console. 

## Motivation

- Python 2 won't be supported past 2020 

    <img src="http://bestanimations.com/HomeOffice/Clocks/Grandfather/old-grandfather-clock-animated-gif-7.gif#.W1J27VgRJQ4.link" width=100> [tic tac tic tac...](https://pythonclock.org/)

- Division in Python 3 always returns a `float`; whereas division in Python 2 can return an `int`
- Critical for large Python 2 code bases that perform division operations



## Requirements
- Python 3

## Install

### Method 1: Install from [Pypi](https://pypi.org/) Method

```
pip3 install shldn
```

Or, if you use [pipenv](https://docs.pipenv.org/),
```
pipenv install shldn
```

### Method 2: Clone repository
Move to the desired directory to install [shldn](https://github.com/NablaZeroLabs/shldn)

```
git clone https://github.com/NablaZeroLabs/shldn.git
```

## Usage

### Method 1 (Installed from [Pypi](https://pypi.org/)):
In environment installed: 
1. Check if installed 
```
pip list
```
2. Execute
```
shldn [-h] [-hr] [-r] path
```

### Method 2 (Cloned repo):
1. Execute
```
python3 leonard.py [-h] [-hr] [-r] path

```
#### Arguments 
```
positional arguments:
  path                  path to python source file(s)

optional arguments:
  -h, --help            show this help message and exit
  -hr, --human_readable
                        set for friendlier output
  -r, --recursive       recursively check python files in path
```

## License
This project is licensed under the MIT License - see the [LICENSE.txt](https://github.com/NablaZeroLabs/shldn/blob/master/LICENSE.txt) file for details.

## More Resources
- [Porting Python 2 Code to Python 3](https://docs.python.org/3/howto/pyporting.html) by Brett Cannon