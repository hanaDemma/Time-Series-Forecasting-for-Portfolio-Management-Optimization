import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
import numpy as np # type: ignore

def preprocess_data(data,ticker):
    print(f"{ticker} Missing values:\n{data.isnull().sum()}")
    data.reset_index(inplace=True)
    return data