from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QLabel, QComboBox, QHBoxLayout
)


def create_ml_screen(app):
    widget = QWidget()
    layout = QVBoxLayout()

    top = QHBoxLayout()
    back = QPushButton("← Voltar")
    back.clicked.connect(app.open_menu_screen)

    top.addWidget(back)
    top.addStretch()

    title = QLabel("Regressão Linear")

    load_btn = QPushButton("Carregar dataset")
    load_btn.clicked.connect(app.prepare_ml_dataset)

    app.target_combo = QComboBox()
    app.target_combo.setEnabled(False)

    train_btn = QPushButton("Treinar")
    train_btn.clicked.connect(app.train_model)

    app.ml_result = QLabel("Nenhum modelo treinado.")

    layout.addLayout(top)
    layout.addWidget(title)
    layout.addWidget(load_btn)
    layout.addWidget(app.target_combo)
    layout.addWidget(train_btn)
    layout.addWidget(app.ml_result)
    layout.addStretch()

    widget.setLayout(layout)
    return widget
