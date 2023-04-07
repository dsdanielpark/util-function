# utilfunc
The Python package utilfunc wraps and distributes useful functions in an easy-to-use way. We have collected functions that are simpler in function than many distributed Python packages or whose category is ambiguous.

<br>

# Installation
```
pip install utilfunc
```

<br>

# Features
`path_finder.py`: Find the path of a file or folder. 
```python
from utilfunc import find_path

nii_file_list = find_path('./home', 'file', 'mask.nii.gz')
```

<br>

# How to Contribute
Please create a pull request for any function that is useful and simple to reuse. Create a function, and write a tutorial with the same name as the function in the doc folder. Any snippet that you are comfortable with and use often will do. However, some contents may be revised and adjusted later for convenience.

1. Create a Python file containing functions in [`utilfunc folder`](https://github.com/DSDanielPark/utilfunc/tree/main/utifunc). You must include formatting and doc strings in your function.
2. Write brief explanations and examples in the [`doc folder`](https://github.com/DSDanielPark/utilfunc/tree/main/doc)
3. Write a one-line code example in README.md
5. Make a Pull Request
Please refer to the find_path function in path_finder.py.

<br>

# Notice
- This repo goes through a simple QA process, there are no major refactoring plans, and it's not a planned project, so it's in alpha.
- If there is a reference, please list it at the top of each Python file.