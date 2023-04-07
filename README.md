# util-functions
![Util-Func](https://img.shields.io/badge/pypi-utilfunctions-blue)
![Pypi Version](https://img.shields.io/pypi/v/utilfunctions.svg)
[![Contributor Covenant](https://img.shields.io/badge/contributor%20covenant-v2.0%20adopted-black.svg)](code_of_conduct.md)
[![Python Version](https://img.shields.io/badge/python-3.6%2C3.7%2C3.8-black.svg)](code_of_conduct.md)
![Code convention](https://img.shields.io/badge/code%20convention-pep8-black)

The Python package utilfunctions wraps and distributes useful functions in an easy-to-use way. We have collected functions that are simpler in function than many distributed Python packages or whose category is ambiguous.

<br>

# Installation
```
pip install utilfunctions
```

<br>

# Features
`path_finder.py`: Find the path of a file or folder. 
```python
from utilfunctions import find_path

nii_file_list = find_path('./home', 'file', 'mask.nii.gz')
```

<br>

# How to Contribute
Please create a pull request for any function that is useful and simple to reuse. Create a function, and write a tutorial with the same name as the function in the doc folder. Any snippet that you are comfortable with and use often will do. However, some contents may be revised and adjusted later for convenience.

1. Create a Python file containing functions in [`utilfunctions folder`](https://github.com/DSDanielPark/utilfunctions/tree/main/utifunc). You must include formatting and doc strings in your function.
2. Write brief explanations and examples in the [`doc folder`](https://github.com/DSDanielPark/utilfunctions/tree/main/doc)
3. Write a one-line code example in README.md
5. Make a Pull Request
<br>

Please refer to the `find_path` function in [`path_finder.py`](https://github.com/DSDanielPark/utilfunctions/blob/main/utifunc/path_finder.py).

<br>

# Notice
- This repo goes through a simple QA process, there are no major refactoring plans, and it's not a planned project, so it's in alpha.
- If there is a reference, please list it at the top of each Python file.
- Coverage of Python versions is subject to change. However, the code formatting is changed to black during the QA process.