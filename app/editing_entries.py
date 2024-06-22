from tkinter import ttk
import tkinter as tk
import customtkinter as ctk
from create_DB import get_cursor
from sqlite3 import Cursor
from typing import Optional, Union, Tuple


class EditEntrie(ctk.CTkToplevel):
    def __init__(
        self,
        data,
        *args,
        fg_color: Optional[Union[str, Tuple[str, str]]] = None,
        **kwargs,
    ):
        super().__init__(*args, fg_color=fg_color, **kwargs)

        (
            self.id,
            self.job_title,
            self.department,
            self.name,
            self.secondname,
            self.surname,
            self.login,
            self.password,
            self.role,
            self.age,
            self.date_birth,
            self.vacation,
            self.retirment,
            self.pre_retirment,
            self.childless,
            self.many_childrens,
            self.veteran,
        ) = data

        self.__add_widgets()

    def __add_labels(self, frame: ctk.CTkFrame):
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

    def __add_widgets(self) -> None:
        from usefull_functions import (
            JOB_TITLE,
            DEPARTMENTS,
            CHOICES_FOR_ROLE,
            CHOICES_FOR_STATUS,
        )

        ctk.CTkLabel(
            self, text="Редактирование пользователей", font=("Arial", 28)
        ).pack(pady=20, padx=50)

        frame = ctk.CTkFrame(self)
        frame.pack(pady=15)

        self.__add_labels(frame)

        self.StringVar_name = tk.StringVar(frame, value=self.name)
        name = ttk.Entry(frame, textvariable=self.StringVar_name)
        name.grid(row=0, column=1)

        self.StringVar_secondname = tk.StringVar(frame, value=self.secondname)
        secondname = ttk.Entry(frame, textvariable=self.StringVar_secondname)
        secondname.grid(row=1, column=1)

        self.StringVar_surname = tk.StringVar(frame, value=self.surname)
        surname = ttk.Entry(frame, textvariable=self.StringVar_surname)
        surname.grid(row=2, column=1)

        self.StringVar_age = tk.StringVar(frame, value=self.age)
        age = ttk.Entry(frame, textvariable=self.StringVar_age)
        age.grid(row=3, column=1)

        self.StringVar_department = tk.StringVar(frame, value=self.department)
        ctk.CTkOptionMenu(
            frame, variable=self.StringVar_department, values=DEPARTMENTS
        ).grid(row=4, column=1)

        self.StringVar_job_title = tk.StringVar(frame, value=self.job_title)
        ctk.CTkOptionMenu(
            frame, variable=self.StringVar_job_title, values=JOB_TITLE
        ).grid(row=5, column=1)

        self.StringVar_date_birth = tk.StringVar(frame, value=self.date_birth)
        date_birth = ttk.Entry(frame, textvariable=self.StringVar_date_birth)
        date_birth.grid(row=6, column=1)

        self.StringVar_role = tk.StringVar(frame, value=self.role)
        ctk.CTkOptionMenu(
            frame, variable=self.StringVar_role, values=CHOICES_FOR_ROLE
        ).grid(row=7, column=1)

        self.StringVar_veteran = tk.StringVar(frame, self.veteran)
        ctk.CTkOptionMenu(
            frame, variable=self.StringVar_veteran, values=CHOICES_FOR_STATUS
        ).grid(row=8, column=1)

        self.StringVar_many_childrens = tk.StringVar(frame, value=self.many_childrens)
        ctk.CTkOptionMenu(
            frame,
            variable=self.StringVar_many_childrens,
            values=CHOICES_FOR_STATUS,
        ).grid(row=9, column=1)

        self.StringVar_childless = tk.StringVar(frame, self.childless)
        ctk.CTkOptionMenu(
            frame, variable=self.StringVar_childless, values=CHOICES_FOR_STATUS
        ).grid(row=10, column=1)

        self.StringVar_retirment = tk.StringVar(frame, value=self.retirment)
        ctk.CTkOptionMenu(
            frame, variable=self.StringVar_retirment, values=CHOICES_FOR_STATUS
        ).grid(row=11, column=1)

        self.StringVar_pre_retirment = tk.StringVar(frame, value=self.pre_retirment)
        ctk.CTkOptionMenu(
            frame, variable=self.StringVar_pre_retirment, values=CHOICES_FOR_STATUS
        ).grid(row=12, column=1)

        self.StringVar_vacation = tk.StringVar(frame, value=self.vacation)
        ctk.CTkOptionMenu(
            frame, variable=self.StringVar_vacation, values=CHOICES_FOR_STATUS
        ).grid(row=13, column=1)

        self.StringVar_login = tk.StringVar(frame, value=self.login)
        login = ttk.Entry(frame, textvariable=self.StringVar_login)
        login.grid(row=14, column=1)

        self.StringVar_password = tk.StringVar(frame, value=self.password)
        password = ttk.Entry(frame, textvariable=self.StringVar_password)
        password.grid(row=15, column=1)
        ctk.CTkButton(self, text="Применить", command=self.__save_changes).pack(pady=20)

    def __save_changes(self):
        cursor = get_cursor()

        self.__update_employees(cursor)
        self.__update_employees_and_positions(cursor)

        cursor.connection.commit()
        self.destroy()

    def __update_employees_and_positions(self, cursor: Cursor):

        cursor.execute(
            f"""
                        SELECT id FROM employees
                        WHERE login = "{self.login}" AND
                        password = "{self.password}"
                        """
        )

        user_id = list(cursor.fetchone())

        cursor.execute(
            f"""
                        SELECT id FROM job_title
                        WHERE name = "{self.StringVar_job_title.get()}"
                        """
        )

        id_job_title = list(cursor.fetchone())

        cursor.execute(
            f"""
                        SELECT id FROM department
                        WHERE name = "{self.StringVar_department.get()}"
                        """
        )

        id_department = list(cursor.fetchone())

        cursor.execute(
            f"""
                        UPDATE employees_and_positions
                        SET id_job_title = "{id_job_title[0]}",
                            id_department = "{id_department[0]}"

                        WHERE id_employee = "{user_id[0]}"
                        """
        )

        cursor.connection.commit()

    def __update_employees(self, cursor: Cursor):

        cursor.execute(
            f"""
                        SELECT id FROM employees
                        WHERE login = "{self.login}" AND
                        password = "{self.password}"
                        """
        )

        user_id = list(cursor.fetchone())

        cursor.execute(
            f"""
                        UPDATE employees
                        SET name = "{self.StringVar_name.get()}",
                            second_name = "{self.StringVar_secondname.get()}",
                            surname = "{self.StringVar_surname.get()}",
                            login = "{self.StringVar_login.get()}",
                            password = "{self.StringVar_password.get()}",
                            role = "{self.StringVar_role.get()}",
                            age = "{self.StringVar_age.get()}",
                            date_birth = "{self.StringVar_date_birth.get()}",
                            status_vacation = "{self.StringVar_vacation.get()}",
                            status_retirement = "{self.StringVar_retirment.get()}",
                            status_pre_retirement = "{self.StringVar_pre_retirment.get()}",
                            status_childless = "{self.StringVar_childless.get()}",
                            status_many_children = "{self.StringVar_many_childrens.get()}",
                            status_veteran = "{self.StringVar_veteran.get()}"
                        WHERE id = {user_id[0]}
                        """
        )
