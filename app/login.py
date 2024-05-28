import tkinter as tk
from create_DB import CreateDataBase

department = ''
class Login(tk.Tk):
    """
    Класс для страницы со входом в систему
    """

    def __init__(
        self,
        screenName: str | None = None,
        baseName: str | None = None,
        className: str = "Tk",
        useTk: bool = True,
        sync: bool = False,
        use: str | None = None,
    ) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.geometry("370x420")
        self.title("Login")
        self.resizable(height=False, width=False)
        
        db = CreateDataBase()
        self.cursor = db.get_cursor()

        self.__add_widgets()
     
        self.mainloop()

    def __add_widgets(self):
        """
        Функция для добавления виджетов на экран
        """

        # Создаем виджеты
        logo_label = tk.Label(self, text="Вход", font=("Arial", 50))
        label_for_login = tk.Label(self, text="Логин: ", font=("Arial", 22))
        self.entry_for_login = tk.Entry(self, font=("Arial", 16))
        label_for_password = tk.Label(self, text="Пароль: ", font=("Arial", 22))
        self.entry_for_password = tk.Entry(self, show="*", font=("Arial", 16))
        button_login = tk.Button(self, text="Войти", command=self.get_role)

        # Размещаем их
        logo_label.pack(pady=30)
        label_for_login.pack()
        self.entry_for_login.pack()
        label_for_password.pack()
        self.entry_for_password.pack()
        button_login.pack(pady=15)

    def __check_user(self) -> str:
        """
        Проверка на пользователя с введенными данными
        """
        
        # Получаем данные с наших полей ввода
        self.login: str = self.entry_for_login.get()
        self.password: str = self.entry_for_password.get()


        # Делаем выборку по введенным данным
        try:
            self.cursor.execute(
                f"""
                SELECT role FROM employees
                WHERE password='{self.password}' AND login='{self.login}'
                """
            )

            # Получаем роль пользователя
            role: list[str] = list(self.cursor.fetchone())
            
            
        
        except Exception:
            # Выводим надпись, что пользователь не найден
            tk.Label(self, text='Пользователь не найден', fg='red').pack()

            text_null1 = tk.StringVar(self, '')
            text_null2 = tk.StringVar(self, '')

            # Убираем текст из полей ввода
            self.entry_for_login.configure(textvariable=text_null1)
            self.entry_for_password.configure(textvariable=text_null2)

        # Проверка на то, что мы ТОЧНО получили роль
        if role is not None:
            return role[0]

    def get_role(self) -> str:
        """
        Функция для получения роли
        """
        role: str = self.__check_user()
        if role is not None:
            self.quit()
            return role
    
