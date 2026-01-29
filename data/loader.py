import pandas as pd

def load_csv(path):
    """
    Carrega um arquivo CSV e retorna um DataFrame.
    """
    return pd.read_csv(path)
