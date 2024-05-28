from login import Login
from admin_panel import Admin_panel
from teacher_page import TeacherPanel
from staff_page import StaffPanel

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

        self.login = Login()
        role, self.department= self.login.get_role()
        
        if role is not None:
            self.__redirect_to_page(role)
            

    def __redirect_to_page(self, role: str):
        """
        Метод для перенаправления на страницы по роли
        """
        if role == 'admin':
            # Перенаправить на страницу с ролью admin
            self.login.destroy()
            Admin_panel()           

        elif role == 'teacher':
            # Перенаправить на страницу с ролью teacher
            self.login.destroy()
            TeacherPanel(*self.department)


        elif role == 'staff':
            # Перенаправить на страницу с ролью staff
            self.login.destroy()
            StaffPanel(*self.department)




if __name__ == "__main__":
    MainApp()
