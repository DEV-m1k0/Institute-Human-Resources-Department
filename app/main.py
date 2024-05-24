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

        login = Login()
        role: str = login.get_role()
        
        if role is not None:
            self.__redirect_to_page(role)
            

    def __redirect_to_page(self, role: str):
        """
        Метод для перенаправления на страницы по роли
        """
        if role == 'admin':
            print(f"Ваша роль: {role}")
            # Перенаправить на страницу с ролью admin
            pass

        elif role == 'teacher':
            print(f"Ваша роль: {role}")
            # Перенаправить на страницу с ролью teacher
            pass

        elif role == 'staff':
            print(f"Ваша роль: {role}")
            # Перенаправить на страницу с ролью staff
            pass


if __name__ == "__main__":
    MainApp()
