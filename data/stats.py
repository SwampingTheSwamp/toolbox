def dataset_stats(df):
    """
    Retorna estatísticas básicas do DataFrame.
    """
    return {
        "linhas": df.shape[0],
        "colunas": df.shape[1],
        "nulos": int(df.isnull().sum().sum()),
        "colunas_numericas": list(df.select_dtypes(include="number").columns),
        "colunas_texto": list(df.select_dtypes(exclude="number").columns)
    }
