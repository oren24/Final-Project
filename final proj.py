# %% md

# Exercise 4 - Advanced Programming in Python

### Topic: Data processing and analysis 

#### Libraries in use:
Numpy, Pandas, Matplotlib

# %% md

### written by:

Oren
Drori
316081884

Rotem
Mihailovitch
316217538

# %%


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as skl


# %%

data=None
try:
    data = pd.DataFrame(pd.read_excel("flights.xlsx"))
    print("file Loaded.")
except Exception as bug:
    print("Error occurred:", bug)


# %%

