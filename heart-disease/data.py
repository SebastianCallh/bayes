"""Data"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def load_train_and_test(frac_test: float) -> pd.DataFrame:
    df = pd.read_csv('heart.csv')
    X = df.drop(['target'], axis=1)
    y = df.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=frac_test, stratify = df.target)

    return (X_train, y_train), (X_test, y_test)
