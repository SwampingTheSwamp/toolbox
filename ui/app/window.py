from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QTableWidgetItem
)

from ui.app.screens.menu import create_menu_screen
from ui.app.screens.data_screen import create_data_screen
from ui.app.screens.ml_screen import create_ml_screen

from ui.app.controllers.navigation import NavigationController
from ui.app.controllers.actions import ActionController


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Toolbox")
        self.setMinimumSize(900, 600)

        self.current_df = None

        self.stack = QStackedWidget()

        # Controllers
        NavigationController(self)
        ActionController(self)

        # Screens
        self.menu_screen = create_menu_screen(self)
        self.data_screen = create_data_screen(self)
        self.ml_screen = create_ml_screen(self)

        self.stack.addWidget(self.menu_screen)
        self.stack.addWidget(self.data_screen)
        self.stack.addWidget(self.ml_screen)

        self.setCentralWidget(self.stack)

    # =================================================
    # TABELA
    # =================================================

    def load_table(self, df):
        self.table.setRowCount(df.shape[0])
        self.table.setColumnCount(df.shape[1])
        self.table.setHorizontalHeaderLabels(df.columns)

        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                value = str(df.iat[row, col])
                self.table.setItem(row, col, QTableWidgetItem(value))
