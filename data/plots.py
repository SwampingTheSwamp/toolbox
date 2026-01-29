import matplotlib.pyplot as plt

def plot_numeric_columns(df):
    """
    Cria um gráfico simples com média das colunas numéricas.
    """
    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        return None

    means = numeric_df.mean()

    fig = plt.figure(figsize=(6,4))
    means.plot(kind="bar")
    plt.title("Média das Colunas Numéricas")
    plt.ylabel("Valor médio")
    plt.tight_layout()

    return fig
