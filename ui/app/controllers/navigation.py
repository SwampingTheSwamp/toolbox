class NavigationController:

    def __init__(self, app):
        app.open_menu_screen = lambda: app.stack.setCurrentIndex(0)
        app.open_data_screen = lambda: app.stack.setCurrentIndex(1)
        app.open_ml_screen = lambda: app.stack.setCurrentIndex(2)
