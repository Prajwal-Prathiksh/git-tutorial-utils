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
- `.github/workflows/pep8-check.yaml`: Contains the details for the GitHub Action to check the code for PEP8 compliance on every push/PR.
- `.github/workflows/run-tests.yaml`: Contains the details for the GitHub Action to run pytest on the code on every push/PR.
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


## Template Examples of PRs
- [PR #1: Feat adv arithmetic operators good pr](https://github.com/Prajwal-Prathiksh/git-tutorial-utils/pull/1)
  - This is a PR that showcases the addition of advanced arithmetic operators to the `arithmetic.py` module.
  - It has also added the tests for the same in the `test_arithmetic.py` module.
  - The PR does not have any conflicts, breaks the code, fails the linting checks, or fails the tests.
  - The PR passes all the checks and is ready to be merged.
- [PR #2: Feat adv arithmetic operators bad pr](https://github.com/Prajwal-Prathiksh/git-tutorial-utils/pull/2)
  - This is a PR that showcases the addition of advanced arithmetic operators to the `arithmetic.py` module.
  - It has not updated the tests for the same in the `test_arithmetic.py` module.
  - The code update breaks existing functionality, fails the linting checks, and fails the tests.
  - The PR does not pass all the checks and cannot be merged unless branch protection rules are overridden.
  - This PR, however, is a good example of how a PR should not be made.
  - The follow-up options are to either fix the PR with the required changes or close the PR.
- [PR #3: Feat add circle area](https://github.com/Prajwal-Prathiksh/git-tutorial-utils/pull/3)
  - This is a PR that showcases the addition of functions power in `arithmetic.py` and circle_area in `geometry.py` modules.
  - It has also added the tests for the same in the `test_arithmetic.py` and `test_geometry.py` modules.
  - The PR does not have any conflicts, breaks the code, fails the linting checks, or fails the tests **(AS OF NOW)!**
  - This PR passes all the checks and is ready to be merged.
  - However, this PR is meant to showcase how potential merge conflicts can prop up.
  - This PR modifies the certain clocks of code which are also changed by `PR #1`. So if `PR #1` is merged into the `main` branch, this PR will have merge conflicts, or vice-versa.
  > In such scenarios, the following options are available for the maintainers:
  > - Notify both the contributors about this issue, so either of them can rebase their branch on top of the other, to resolve the conflicts.
  > - Merge the more complex PR first, and then rebase the simpler PR on top of the `main` branch. On any conflicts, either the maintainer or the contributor of the simpler PR can resolve the conflicts.
  > - Close both the PRs do it all themselves :) Just kidding, don't do this unless you like suffering.