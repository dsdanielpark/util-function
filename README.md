Development Status :: 3 - Alpha

# util-function
![Util-Func](https://img.shields.io/badge/pypi-utilfunction-orange)
![Pypi Version](https://img.shields.io/pypi/v/utilfunction.svg)
[![Contributor Covenant](https://img.shields.io/badge/contributor%20covenant-v2.0%20adopted-black.svg)](code_of_conduct.md)
[![Python Version](https://img.shields.io/badge/python-3.6%2C3.7%2C3.8-black.svg)](code_of_conduct.md)
![Code convention](https://img.shields.io/badge/code%20convention-pep8-black)

The Python package utilfunction wraps and distributes useful functions in an easy-to-use way. We have collected functions that are simpler in function than many distributed Python packages or whose category is ambiguous.

<br>

# Installation
```
pip install utilfunction
```

<br>

# Features
`path_finder.py` - function: find_path <br>
 Find the path of a file or folder. 
```python
from utilfunction import find_path

nii_file_list = find_path('./home', 'file', 'mask.nii.gz')
```
<br>

`astyper.py` - function: col_converter <br>
Restores a column whose array is stored as a string type back to an array type.
```python
from utilfunction import col_convert

df_has_converted_col = col_convert(df, "embedding_arrays")
```

<br>

`beep.py` - function: beep <br>
Make beep
```python
from utilfunction import beep

beep()

sec=10
feq=800
beep(sec, feq)
```

<br>

# How to Contribute
Please create a pull request for any function that is useful and simple to reuse. Create a function, and write a tutorial with the same name as the function in the doc folder. Any snippet that you are comfortable with and use often will do. However, some contents may be revised and adjusted later for convenience.

1. Create a Python file containing functions in [`utilfunction folder`](https://github.com/DSDanielPark/utilfunction/tree/main/utifunc). You must include formatting and doc strings in your function.
2. Write brief explanations and examples in the [`doc folder`](https://github.com/DSDanielPark/utilfunction/tree/main/doc)
3. Write a one-line code example in README.md
5. Make a Pull Request
<br>

Please refer to the `find_path` function in [`path_finder.py`](https://github.com/DSDanielPark/utilfunction/blob/main/utifunc/path_finder.py).

<br>

# Notice
- This repo goes through a simple QA process, there are no major refactoring plans, and it's not a planned project, so it's in alpha.
- If there is a reference, please list it at the top of each Python file.
- Coverage of Python versions is subject to change. However, the code formatting is changed to black during the QA process.
