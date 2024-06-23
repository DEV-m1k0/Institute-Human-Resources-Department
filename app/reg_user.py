from typing import Tuple, Optional, Union
from tkinter import ttk
import customtkinter as ctk
import tkinter as tk
from create_DB import get_cursor
from sqlite3 import Cursor


class RegistrationUsers(ctk.CTk):
    def __init__(
        self, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kwargs
    ):
        super().__init__(fg_color, **kwargs)
        self.geometry("500x700")
        self.resizable(width=False, height=False)
        self.title("Registration")

        self.__add_widgets()
        self.mainloop()

    def __add_widgets(self):
        """
        Функция для добавления виджетов
        """

        ctk.CTkButton(self, text="<- Назад", command=self.__back).pack()

        main_title_label = ctk.CTkLabel(
            self, text="Регистрация пользователей", font=("Arial", 28)
        )
        main_title_label.pack()

        frame = ctk.CTkFrame(self)
        frame.pack(pady=20)

        self.__label_pack(frame)
        self.__entry_pack(frame)

        ctk.CTkButton(self, text="Зарегестрировать", command=self.__reg).pack(pady=3)

    def __reg(self):

        cursor = get_cursor()

        self.__insert_into_employees(cursor)
        self.__insert_into_empoyees_and_positions(cursor)

        cursor.connection.commit()

    def __insert_into_empoyees_and_positions(self, cursor: Cursor):

        cursor.execute(
            f"""
                        SELECT id FROM employees
                        WHERE login = "{self.entry_login.get()}"
                        AND password = "{self.entry_password.get()}"
                        """
        )

        employee_id = list(cursor.fetchone())

        cursor.execute(
            f"""
                        SELECT id FROM job_title
                        WHERE name = "{self.stringVar_job_title.get()}"
                        """
        )

        job_title_id = list(cursor.fetchone())

        cursor.execute(
            f"""
                        SELECT id FROM department
                        WHERE name = "{self.stringVar_department.get()}"
                        """
        )

        department_id = list(cursor.fetchone())

        cursor.execute(
            f"""
                        INSERT INTO employees_and_positions (id_employee, id_job_title, id_department)
                        VALUES ({employee_id[0]}, {job_title_id[0]}, {department_id[0]})
                       """
        )

    def __insert_into_employees(self, cursor: Cursor):
        role = ""

        if self.stringVar_position.get() == "Администрация":
            role = "admin"

        elif self.stringVar_position.get() == "Преподаватель":
            role = "teacher"

        elif self.stringVar_position.get() == "Технический персонал":
            role = "staff"

        cursor.execute(
            f"""
                        INSERT INTO employees(name, second_name, surname, login, password,
                        role, age, date_birth, status_vacation, status_retirement,
                        status_pre_retirement, status_childless, status_many_children,
                        status_veteran)
                        VALUES ("{self.entry_name.get()}", "{self.entry_secondname.get()}",
                        "{self.entry_surnmae.get()}", "{self.entry_login.get()}",
                        "{self.entry_password.get()}", "{role}",
                        "{self.entry_age.get()}", "{self.entry_date_birth.get()}",
                        "{self.stringVar_vacation.get()}", "{self.stringVar_retirement.get()}",
                        "{self.stringVar_pre_retiremen.get()}", "{self.stringVar_childless.get()}",
                        "{self.stringVar_many_children.get()}", "{self.stringVar_veteran.get()}")
                       """
        )

    def __back(self):

        self.quit()
        self.destroy()

        from admin_panel import Admin_panel

        Admin_panel()

    def __label_pack(self, frame: ctk.CTkFrame) -> None:
        """
        Функция для размещения на странице лэйблов
        """

        labels = [
            "Имя: ",
            "Фамилия: ",
            "Отчество: ",
            "Возраст: ",
            "Департамент: ",
            "Должность: ",
            "Дата Рождения: ",
            "Позиция: ",
            "Ветеран: ",
            "Многодетный: ",
            "Бездетный",
            "Пенсионер: ",
            "Предпенсионный возраст: ",
            "В отпуске: ",
            "Логин: ",
            "Пароль: ",
        ]

        count = 0
        for name_label in labels:
            ctk.CTkLabel(frame, text=name_label).grid(row=count, column=0, pady=3)
            count += 1

    def __entry_pack(self, frame: tk.Frame) -> None:
        """
        Функция для размещения на странице entry
        """

        from usefull_functions import (
            DEPARTMENTS,
            JOB_TITLE,
            CHOICES_FOR_ROLE,
            CHOICES_FOR_STATUS,
        )

        self.entry_name: ttk.Entry = ttk.Entry(frame)
        self.entry_name.grid(row=0, column=1)

        self.entry_secondname: ttk.Entry = ttk.Entry(frame)
        self.entry_secondname.grid(row=1, column=1)

        self.entry_surnmae: ttk.Entry = ttk.Entry(frame)
        self.entry_surnmae.grid(row=2, column=1)

        self.entry_age: ttk.Entry = ttk.Entry(frame)
        self.entry_age.grid(row=3, column=1)

        self.stringVar_department = tk.StringVar(frame)
        self.stringVar_department.set(DEPARTMENTS[0])
        entry_department = ctk.CTkOptionMenu(
            frame, variable=self.stringVar_department, values=DEPARTMENTS
        )
        entry_department.grid(row=4, column=1)

        self.stringVar_job_title = tk.StringVar(frame)
        self.stringVar_job_title.set(JOB_TITLE[0])
        entry_job_title = ctk.CTkOptionMenu(
            frame, variable=self.stringVar_job_title, values=JOB_TITLE
        )
        entry_job_title.grid(row=5, column=1)

        self.entry_date_birth: ttk.Entry = ttk.Entry(frame)
        self.entry_date_birth.grid(row=6, column=1)

        self.stringVar_position = tk.StringVar(frame)
        self.stringVar_position.set(CHOICES_FOR_ROLE[0])
        entry_position = ctk.CTkOptionMenu(
            frame, variable=self.stringVar_position, values=CHOICES_FOR_ROLE
        )
        entry_position.grid(row=7, column=1)

        self.stringVar_veteran = tk.StringVar(frame)
        self.stringVar_veteran.set(CHOICES_FOR_STATUS[0])
        entry_veteran = ctk.CTkOptionMenu(
            frame, variable=self.stringVar_veteran, values=CHOICES_FOR_STATUS
        )
        entry_veteran.grid(row=8, column=1)

        self.stringVar_many_children = tk.StringVar(frame)
        self.stringVar_many_children.set(CHOICES_FOR_STATUS[0])
        entry_many_children = ctk.CTkOptionMenu(
            frame, variable=self.stringVar_many_children, values=CHOICES_FOR_STATUS
        )
        entry_many_children.grid(row=9, column=1)

        self.stringVar_childless = tk.StringVar(frame)
        self.stringVar_childless.set(CHOICES_FOR_STATUS[0])
        entry_childless = ctk.CTkOptionMenu(
            frame, variable=self.stringVar_childless, values=CHOICES_FOR_STATUS
        )
        entry_childless.grid(row=10, column=1)

        self.stringVar_retirement = tk.StringVar(frame)
        self.stringVar_retirement.set(CHOICES_FOR_STATUS[0])
        entry_retirement = ctk.CTkOptionMenu(
            frame, variable=self.stringVar_retirement, values=CHOICES_FOR_STATUS
        )
        entry_retirement.grid(row=11, column=1)

        self.stringVar_pre_retiremen = tk.StringVar(frame)
        self.stringVar_pre_retiremen.set(CHOICES_FOR_STATUS[0])
        entry_pre_retirement = ctk.CTkOptionMenu(
            frame, variable=self.stringVar_pre_retiremen, values=CHOICES_FOR_STATUS
        )
        entry_pre_retirement.grid(row=12, column=1)

        self.stringVar_vacation = tk.StringVar(frame)
        self.stringVar_vacation.set(CHOICES_FOR_STATUS[0])
        entry_vacation = ctk.CTkOptionMenu(
            frame, variable=self.stringVar_vacation, values=CHOICES_FOR_STATUS
        )
        entry_vacation.grid(row=13, column=1)

        self.entry_login: ttk.Entry = ttk.Entry(frame)
        self.entry_login.grid(row=14, column=1)

        self.entry_password: ttk.Entry = ttk.Entry(frame)
        self.entry_password.grid(row=15, column=1)