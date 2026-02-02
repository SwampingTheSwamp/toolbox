from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel


def create_menu_screen(app):
    widget = QWidget()
    layout = QVBoxLayout()

    title = QLabel("TOOLBOX")

    btn_data = QPushButton("Módulo de Dados")
    btn_data.clicked.connect(app.open_data_screen)

    btn_ml = QPushButton("Módulo de ML")
    btn_ml.clicked.connect(app.open_ml_screen)

    layout.addWidget(title)
    layout.addWidget(btn_data)
    layout.addWidget(btn_ml)
    layout.addStretch()

    widget.setLayout(layout)
    return widget
