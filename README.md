# git-tutorial-utils
A supplementary repository, containing some basic examples for someone to play and learn git.

> Refer to the Git Tutorial [here](https://github.com/Prajwal-Prathiksh/git-tutorial) for a detailed explanation.


## Hands-on Description
This hands-on tutorial is designed to help you show how to best make use of Git and GitHub in a practical way, through a very simple python module.
The tree structure of the repository is as follows:
```bash
.
├── .flake8
├── .github
│   └── workflows
│       ├── pep8-check.yaml
│       └── run-tests.yaml
├── .gitignore
├── LICENSE
├── README.md
├── calculator.ipynb
├── environment.yml
├── pyproject.toml
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── arithmetic.py
│   └── geometry.py
└── tests
    ├── __init__.py
    ├── test_arithmetic.py
    └── test_geometry.py
```


## In-depth explanation of the files
- `.flake8`: Contains the details for `flake8` linter.
- `.github/workflows/pep8-check.yaml`: Contains the details for the GitHub Action to check the code for PEP8 compliance.
- `.github/workflows/run-tests.yaml`: Contains the details for the GitHub Action to run pytest on the code.
- `.gitignore`: Contains the details for the files to be ignored by git.
- `calculator.ipynb`: A Jupyter notebook containing the examples for the python module, showcasing how to import and use the `src` module.
- `environment.yml`: Contains the environment details for the conda environment. Can be used to create a new conda environment by running:
```bash
conda env create -f environment.yml
```
- `pyproject.toml`: Contains the details for `pyright` linter.
- `requirements.txt`: Contains the environment details for the pip environment. Can be used to create a new pip environment by running:
```bash
pip install -r requirements.txt
```
- `src/__init__.py`: The `__init__.py` file to make the `src` directory a package.
- `src/arithmetic.py`: Contains the arithmetic functions.
- `src/geometry.py`: Contains the geometry functions.
- `tests/__init__.py`: The `__init__.py` file to make the `tests` directory a package.
- `tests/test_arithmetic.py`: Contains the tests for the arithmetic functions.
- `tests/test_geometry.py`: Contains the tests for the geometry functions.