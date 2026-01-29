import sys
import pandas as pd

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFileDialog,
    QTableWidget,
    QTableWidgetItem,
    QStackedWidget,
    QHBoxLayout
)

from data.loader import load_csv
from data.stats import dataset_stats
from data.plots import plot_numeric_columns


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Toolbox")
        self.setMinimumSize(900, 600)

        self.current_df = None

        self.stack = QStackedWidget()

        self.menu_screen = self.create_menu_screen()
        self.data_screen = self.create_data_screen()

        self.stack.addWidget(self.menu_screen)
        self.stack.addWidget(self.data_screen)

        self.setCentralWidget(self.stack)

    # ---------------------
    # TELAS
    # ---------------------

    def create_menu_screen(self):
        widget = QWidget()
        layout = QVBoxLayout()

        title = QLabel("TOOLBOX")
        title.setStyleSheet("font-size: 26px; font-weight: bold;")

        btn_data = QPushButton("Módulo de Dados")
        btn_data.clicked.connect(self.open_data_screen)

        layout.addWidget(title)
        layout.addWidget(btn_data)
        layout.addStretch()

        widget.setLayout(layout)
        return widget

    def create_data_screen(self):
        widget = QWidget()
        main_layout = QHBoxLayout()

        # Barra superior
        top_layout = QHBoxLayout()

        btn_back = QPushButton("← Voltar")
        btn_back.clicked.connect(self.open_menu_screen)

        btn_open = QPushButton("Abrir CSV")
        btn_open.clicked.connect(self.open_csv)

        btn_plot = QPushButton("Ver Gráfico")
        btn_plot.clicked.connect(self.show_plot)

        top_layout.addWidget(btn_back)
        top_layout.addStretch()
        top_layout.addWidget(btn_open)
        top_layout.addWidget(btn_plot)

        # Tabela
        self.table = QTableWidget()

        # Estatísticas
        self.stats_label = QLabel("Estatísticas:")
        self.stats_label.setStyleSheet("font-size: 14px;")

        self.info_label = QLabel("Nenhum arquivo carregado.")

        # Layout esquerdo
        left_layout = QVBoxLayout()
        left_layout.addLayout(top_layout)
        left_layout.addWidget(self.table)
        left_layout.addWidget(self.info_label)

        # Layout direito
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.stats_label)
        right_layout.addStretch()

        main_layout.addLayout(left_layout, 3)
        main_layout.addLayout(right_layout, 1)

        widget.setLayout(main_layout)
        return widget

    # ---------------------
    # NAVEGAÇÃO
    # ---------------------

    def open_menu_screen(self):
        self.stack.setCurrentIndex(0)

    def open_data_screen(self):
        self.stack.setCurrentIndex(1)

    # ---------------------
    # AÇÕES
    # ---------------------

    def open_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Selecionar CSV",
            "",
            "CSV Files (*.csv)"
        )

        if file_path:
            df = load_csv(file_path)
            self.current_df = df

            self.load_table(df)

            stats = dataset_stats(df)

            self.stats_label.setText(
                "Estatísticas:\n"
                f"Linhas: {stats['linhas']}\n"
                f"Colunas: {stats['colunas']}\n"
                f"Nulos: {stats['nulos']}\n\n"
                "Colunas Numéricas:\n"
                + ", ".join(stats['colunas_numericas']) +
                "\n\nColunas Texto:\n"
                + ", ".join(stats['colunas_texto'])
            )

            rows, cols = df.shape
            self.info_label.setText(
                f"Arquivo: {file_path} | Linhas: {rows} | Colunas: {cols}"
            )

    def show_plot(self):
        if self.current_df is None:
            return

        fig = plot_numeric_columns(self.current_df)
        if fig is None:
            return

        import matplotlib.pyplot as plt
        plt.show()

    def load_table(self, df):
        self.table.setRowCount(len(df))
        self.table.setColumnCount(len(df.columns))
        self.table.setHorizontalHeaderLabels(df.columns)

        for row in range(len(df)):
            for col in range(len(df.columns)):
                self.table.setItem(
                    row,
                    col,
                    QTableWidgetItem(str(df.iloc[row, col]))
                )


# ---------------------
# START
# ---------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
