from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QTableWidget
)


def create_data_screen(app):
    widget = QWidget()
    main = QHBoxLayout()

    top = QHBoxLayout()
    back = QPushButton("← Voltar")
    back.clicked.connect(app.open_menu_screen)

    open_btn = QPushButton("Abrir CSV")
    open_btn.clicked.connect(app.open_csv)

    plot_btn = QPushButton("Ver Gráfico")
    plot_btn.clicked.connect(app.show_plot)

    top.addWidget(back)
    top.addStretch()
    top.addWidget(open_btn)
    top.addWidget(plot_btn)

    app.table = QTableWidget()
    app.stats_label = QLabel("Estatísticas:")

    left = QVBoxLayout()
    left.addLayout(top)
    left.addWidget(app.table)

    right = QVBoxLayout()
    right.addWidget(app.stats_label)
    right.addStretch()

    main.addLayout(left, 3)
    main.addLayout(right, 1)

    widget.setLayout(main)
    return widget
