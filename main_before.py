"""
This is a dummy main file to demonstrate how automated code formatting works.
If you have the following VS code extensions installed:
- `isort`: For sorting imports
- `black`: For formatting code

You can run the following command from the command palette - `Format Document`
"""
import pandas as pd

import numpy as np
import time, os, sys
from src.arithmetic import add

from src.geometry import circle_area
from src.arithmetic import subtract

RADIUS = 5.0

def main():
    print("Hello, World!")
    print(f'The result of 5 + 3 is: {add(    5,3)}')
    print(f'The result of 5 - 3 is: {subtract(5, 3)}')
    print(f'The area of a circle with radius {RADIUS} is: {circle_area(RADIUS)}')




# To add docstring to the below functions, try the following prompt
# "Add docstring to this function in Google style format"
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns   = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("(", "").str.replace(")", "")
    return df

def print_dataframe_as_markdown(df: pd.DataFrame):
    print(df.to_markdown(index=False))



# To add a if-main block to the below function, try the following prompt
# "Add a if-main block to this script to call the main function and the print_dataframe_as_markdown function with a sample dataframe"