import tkinter as tk
from scripts.create_DB import CreateDataBase


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

        self.__add_widgets()

        self.mainloop()

    def __add_widgets(self):
        """
        Функция для добавления виджетов на экран
        """

        logo_label = tk.Label(self, text="Вход", font=("Arial", 50))
        label_for_login = tk.Label(self, text="Логин: ", font=("Arial", 22))
        entry_for_login = tk.Entry(self, font=("Arial", 16))
        label_for_password = tk.Label(self, text="Пароль: ", font=("Arial", 22))
        entry_for_password = tk.Entry(self, show="*", font=("Arial", 16))
        button_login = tk.Button(self, text="Войти", command=self.get_role)

        logo_label.pack(pady=30)

        label_for_login.pack()
        entry_for_login.pack()

        label_for_password.pack()
        entry_for_password.pack()

        button_login.pack(pady=15)

    def get_role(self):
        """
        Функция для получения роли
        """

        db = CreateDataBase()
        cursor = db.get_cursor()

        cursor.execute(
            """

            SELECT * FROM employees;

        """
        )

        text = cursor.fetchall()

        print(text)
