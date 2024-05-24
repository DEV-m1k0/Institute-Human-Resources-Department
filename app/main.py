from login import Login


class MainApp:
    """
    Основной класс для взаимодействия дочерних модулей
    """

    def __init__(self) -> None:
        self.run_app()

    def run_app(self):
        """
        Основной метод для добавления разных модулей
        """

        Login()


if __name__ == "__main__":
    MainApp()
