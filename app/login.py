from tkinter import ttk
import tkinter as tk
from create_DB import get_cursor
import customtkinter as ctk
from typing import Union, Optional, Tuple

department = ""


class Login(ctk.CTk):
    """
    Класс для страницы со входом в систему
    """

    def __init__(
        self, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kwargs
    ):
        super().__init__(fg_color, **kwargs)

        self.geometry("370x420")
        self.title("Login")
        self.resizable(height=False, width=False)

        self.cursor = get_cursor()

        self.__add_widgets()

        self.mainloop()

    def __add_widgets(self):
        """
        Функция для добавления виджетов на экран
        """

        # Создаем виджеты
        logo_label = ctk.CTkLabel(self, text="Вход", font=("Arial", 50))
        label_for_login = ctk.CTkLabel(self, text="Логин: ", font=("Arial", 22))
        self.entry_for_login = ttk.Entry(self, font=("Arial", 16))
        label_for_password = ctk.CTkLabel(self, text="Пароль: ", font=("Arial", 22))
        self.entry_for_password = ttk.Entry(self, show="*", font=("Arial", 16))
        button_login = ctk.CTkButton(self, text="Войти", command=self.get_role)

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
        self.get_department()

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
            tk.Label(self, text="Пользователь не найден", fg="red").pack()

            text_null1 = tk.StringVar(self, "")
            text_null2 = tk.StringVar(self, "")

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
            return role, department

    def get_department(self):
        self.cursor.execute(
            f"""
                SELECT employees_and_positions.id_department FROM employees_and_positions
                inner join employees on employees_and_positions.id_employee = employees.id
                WHERE employees.password='{self.password}' AND employees.login='{self.login}'
                """
        )
        global department
        department = self.cursor.fetchone()
