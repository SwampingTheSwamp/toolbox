from PySide6.QtWidgets import QFileDialog
from data.loader import load_csv
from data.stats import dataset_stats
from data.plots import plot_numeric_columns
from ml.trainer import train_linear_regression


class ActionController:

    def __init__(self, app):
        self.app = app
        app.open_csv = self.open_csv
        app.show_plot = self.show_plot
        app.prepare_ml_dataset = self.prepare_ml_dataset
        app.train_model = self.train_model

    def open_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.app, "Selecionar CSV", "", "CSV Files (*.csv)"
        )

        if file_path:
            df = load_csv(file_path)
            self.app.current_df = df
            self.app.load_table(df)

            stats = dataset_stats(df)
            self.app.stats_label.setText(
                f"Linhas: {stats['linhas']}\n"
                f"Colunas: {stats['colunas']}\n"
                f"Nulos: {stats['nulos']}"
            )

    def show_plot(self):
        if self.app.current_df is None:
            return

        fig = plot_numeric_columns(self.app.current_df)
        if fig:
            import matplotlib.pyplot as plt
            plt.show()

    def prepare_ml_dataset(self):
        if self.app.current_df is None:
            return

        self.app.target_combo.clear()
        self.app.target_combo.addItems(
            self.app.current_df.select_dtypes(include="number").columns
        )
        self.app.target_combo.setEnabled(True)

    def train_model(self):
        target = self.app.target_combo.currentText()
        model, mse = train_linear_regression(self.app.current_df, target)
        self.app.ml_result.setText(f"MSE: {mse:.4f}")
