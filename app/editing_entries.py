from tkinter import ttk
import tkinter as tk
from create_DB import get_cursor
from sqlite3 import Cursor

class EditEntrie(tk.Toplevel):
    def __init__(self, data):
        super().__init__()

        self.id, self.job_title, self.department, self.name, self.secondname, self.surname, self.login, self.password, self.role, self.age, self.date_birth, self.vacation, self.retirment, self.pre_retirment, self.childless, self.many_childrens, self.veteran = data 

        self.__add_widgets()

    def __add_widgets(self) -> None:
        from usefull_functions import JOB_TITLE, DEPARTMENTS, CHOICES_FOR_ROLE, CHOICES_FOR_STATUS

        ttk.Label(self, text='Редактирование пользователей', font='Arial 24 bold').pack(pady=20, padx=50)

        frame = ttk.Frame(self)
        frame.pack(pady=35)

        ttk.Label(frame, text='Вакансия: ').grid(row=0, column=0)
        self.StringVar_job_title = tk.StringVar(frame)
        ttk.OptionMenu(frame, self.StringVar_job_title, self.job_title, *JOB_TITLE).grid(row=0, column=1)

        ttk.Label(frame, text='Отдел: ').grid(row=1, column=0)
        self.StringVar_department = tk.StringVar(frame)
        ttk.OptionMenu(frame, self.StringVar_department, self.department, *DEPARTMENTS).grid(row=1, column=1)

        ttk.Label(frame, text='Имя: ').grid(row=2, column=0)
        self.StringVar_name = tk.StringVar(frame, value=self.name)
        name = ttk.Entry(frame, textvariable=self.StringVar_name)
        name.grid(row=2, column=1)

        ttk.Label(frame, text='Фамилия: ').grid(row=3, column=0)
        self.StringVar_secondname = tk.StringVar(frame, value=self.secondname)
        secondname = ttk.Entry(frame, textvariable=self.StringVar_secondname)
        secondname.grid(row=3, column=1)

        ttk.Label(frame, text='Отчество: ').grid(row=4, column=0)
        self.StringVar_surname = tk.StringVar(frame, value=self.surname)
        surname = ttk.Entry(frame, textvariable=self.StringVar_surname)
        surname.grid(row=4, column=1)

        ttk.Label(frame, text='Логин: ').grid(row=5, column=0)
        self.StringVar_login = tk.StringVar(frame, value=self.login)
        login = ttk.Entry(frame, textvariable=self.StringVar_login)
        login.grid(row=5, column=1)

        ttk.Label(frame, text='Пароль: ').grid(row=6, column=0)
        self.StringVar_password = tk.StringVar(frame, value=self.password)
        password = ttk.Entry(frame, textvariable=self.StringVar_password)
        password.grid(row=6, column=1)

        ttk.Label(frame, text='Роль: ').grid(row=7, column=0)
        self.StringVar_role = tk.StringVar(frame)
        ttk.OptionMenu(frame, self.StringVar_role, self.role, *CHOICES_FOR_ROLE).grid(row=7, column=1)

        ttk.Label(frame, text='Возраст: ').grid(row=8, column=0)
        self.StringVar_age = tk.StringVar(frame, value=self.age)
        age = ttk.Entry(frame, textvariable=self.StringVar_age)
        age.grid(row=8, column=1)

        ttk.Label(frame, text='Дата рождения: ').grid(row=9, column=0)
        self.StringVar_date_birth = tk.StringVar(frame, value=self.date_birth)
        date_birth = ttk.Entry(frame, textvariable=self.StringVar_date_birth)
        date_birth.grid(row=9, column=1)

        ttk.Label(frame, text='Отпуск: ').grid(row=10, column=0)
        self.StringVar_vacation = tk.StringVar(frame)
        ttk.OptionMenu(frame, self.StringVar_vacation, self.vacation, *CHOICES_FOR_STATUS).grid(row=10, column=1)

        ttk.Label(frame, text='Пенсионер: ').grid(row=11, column=0)
        self.StringVar_retirment = tk.StringVar(frame)
        ttk.OptionMenu(frame, self.StringVar_retirment, self.retirment, *CHOICES_FOR_STATUS).grid(row=11, column=1)

        ttk.Label(frame, text='Предпенсионер: ').grid(row=12, column=0)
        self.StringVar_pre_retirment = tk.StringVar(frame)
        ttk.OptionMenu(frame, self.StringVar_pre_retirment, self.pre_retirment, *CHOICES_FOR_STATUS).grid(row=12, column=1)

        ttk.Label(frame, text='Бездетный: ').grid(row=13, column=0)
        self.StringVar_childless = tk.StringVar(frame)
        ttk.OptionMenu(frame, self.StringVar_childless, self.childless, *CHOICES_FOR_STATUS).grid(row=13, column=1)

        ttk.Label(frame, text='Многодетный: ').grid(row=14, column=0)
        self.StringVar_many_childrens = tk.StringVar(frame)
        ttk.OptionMenu(frame, self.StringVar_many_childrens, self.many_childrens, *CHOICES_FOR_STATUS).grid(row=14, column=1)

        ttk.Label(frame, text='Ветеран: ').grid(row=15, column=0)
        self.StringVar_veteran = tk.StringVar(frame)
        ttk.OptionMenu(frame, self.StringVar_veteran, self.veteran, *CHOICES_FOR_STATUS).grid(row=15, column=1)

        ttk.Button(self, text='Применить', command=self.__save_changes).pack(pady=20)

    def __save_changes(self):
        cursor = get_cursor()

        self.__update_employees(cursor)
        self.__update_employees_and_positions(cursor)
        
        cursor.connection.commit()
        self.destroy()

    def __update_employees_and_positions(self, cursor: Cursor):

        cursor.execute(f"""
                        SELECT id FROM employees
                        WHERE login = "{self.login}" AND
                        password = "{self.password}"
                        """)
        
        user_id = list(cursor.fetchone())

        cursor.execute(f"""
                        SELECT id FROM job_title
                        WHERE name = "{self.StringVar_job_title.get()}"
                        """)
        
        id_job_title = list(cursor.fetchone())

        cursor.execute(f"""
                        SELECT id FROM department
                        WHERE name = "{self.StringVar_department.get()}"
                        """)
        
        id_department = list(cursor.fetchone())

        cursor.execute(f"""
                        UPDATE employees_and_positions
                        SET id_job_title = "{id_job_title[0]}",
                            id_department = "{id_department[0]}"

                        WHERE id_employee = "{user_id[0]}"
                        """)
        
        cursor.connection.commit()

    def __update_employees(self, cursor: Cursor):

        cursor.execute(f"""
                        SELECT id FROM employees
                        WHERE login = "{self.login}" AND
                        password = "{self.password}"
                        """)
        
        user_id = list(cursor.fetchone())

        cursor.execute(f"""
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
                        """)