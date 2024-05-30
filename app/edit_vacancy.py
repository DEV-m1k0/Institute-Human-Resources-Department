from tkinter import ttk
import tkinter as tk
from create_DB import get_cursor
from sqlite3 import Cursor

class EditVacancy(tk.Toplevel):
    """
    Всплывающее окно для редактирования вакансий
    """

    def __init__(self, data):
        super().__init__()

        self.resizable(width=False, height=False)

        self.id, self.job_title, self.salary, self.department, self.date_opening, self.date_closing = data

        print(data)

        self.__add_widgets()

    def __add_widgets(self):
        """
        Добвляем виджеты
        """

        ttk.Label(self, text='Редактирование вакансий', font="Arial 24").pack()

        frame = ttk.Frame(self)
        frame.pack()

        self.__add_entreis(frame)
        self.__add_labels(frame)

        ttk.Button(self, text="Применить", command=self.__edit_vacancy).pack(pady=20)

    def __edit_vacancy(self):
        cursor = get_cursor()

        cursor.execute(f"""
                        SELECT id FROM job_title
                        WHERE name = "{self.StringVar_job_title.get()}"
                        """)
        
        job_title_id = list(cursor.fetchone())[0]

        cursor.execute(f"""
                        SELECT id FROM department
                        WHERE name = "{self.StringVar_depatment.get()}"
                        """)
        
        department_id = list(cursor.fetchone())[0]


        cursor.execute(f"""
                        UPDATE job_vacancy
                        SET id_job_title = {job_title_id},
                            id_department = {department_id},
                            vacancy_opening_date = "{self.StringVar_opening_date.get()}",
                            vacancy_closing_date = "{self.StringVar_closing_date.get()}"
                        WHERE id = {self.id}
                        """)
        

        cursor.execute(f"""
                        UPDATE job_title
                        SET salary = {self.StringVar_salary.get()}
                        WHERE id = {job_title_id}
                        """)
        

        cursor.connection.commit()
        self.destroy()
        


    def __add_entreis(self, frame: ttk.Frame):
        """
        Добавляем поля для ввода
        """
        from usefull_functions import JOB_TITLE, DEPARTMENTS

        self.StringVar_job_title = tk.StringVar(frame, value=self.job_title)
        job_title = ttk.OptionMenu(frame, self.StringVar_job_title, self.job_title, *JOB_TITLE)
        job_title.grid(row=0, column=1)

        self.StringVar_salary = tk.StringVar(frame, value=self.salary)
        entry_salary = ttk.Entry(frame, textvariable=self.StringVar_salary)
        entry_salary.grid(row=1, column=1)

        self.StringVar_depatment = tk.StringVar(frame)
        department = ttk.OptionMenu(frame, self.StringVar_depatment, self.department, *DEPARTMENTS)
        department.grid(row=2, column=1)

        self.StringVar_opening_date = tk.StringVar(frame, value=self.date_opening)
        entry_opening_date = ttk.Entry(frame, textvariable=self.StringVar_opening_date)
        entry_opening_date.grid(row=3, column=1)

        self.StringVar_closing_date = tk.StringVar(frame, value=self.date_closing)
        entry_closing_date = ttk.Entry(frame, textvariable=self.StringVar_closing_date)
        entry_closing_date.grid(row=4, column=1)

    def __add_labels(self, frame: ttk.Frame):
        """
        Добавляем надписи
        """

        ttk.Label(frame, text="Должность: ").grid(row=0, column=0)
        ttk.Label(frame, text="Зарплата: ").grid(row=1, column=0)
        ttk.Label(frame, text="Отдел: ").grid(row=2, column=0)
        ttk.Label(frame, text="Дата открытия: ").grid(row=3, column=0)
        ttk.Label(frame, text="Дата закрытия: ").grid(row=4, column=0)