import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Toolbox")
        self.setMinimumSize(600, 400)

        layout = QVBoxLayout()

        title = QLabel("TOOLBOX")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")

        btn_data = QPushButton("Módulo de Dados")
        btn_viz = QPushButton("Módulo de Gráficos")
        btn_ml = QPushButton("Módulo de ML")

        layout.addWidget(title)
        layout.addWidget(btn_data)
        layout.addWidget(btn_viz)
        layout.addWidget(btn_ml)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
