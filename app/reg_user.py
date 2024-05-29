from tkinter import ttk, Tk
import tkinter as tk
from create_DB import CreateDataBase
from sqlite3 import Cursor

class RegistrationUsers(Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.geometry('500x650')
        self.title('Registration')

        self.__add_widgets()

    def __add_widgets(self):
        """
        Функция для добавления виджетов
        """

        ttk.Button(self, text='<- Назад', command=self.__back).pack()

        main_title_label = ttk.Label(self, text="Регистрация пользователей", font="Arial 28")
        main_title_label.pack()

        frame = ttk.Frame(self)
        frame.pack(pady=20)

        self.__label_pack(frame)
        self.__entry_pack(frame)

        ttk.Button(self, text='Зарегестрировать', command=self.__reg).pack(pady=20)

    def __reg(self):

        db = CreateDataBase()
        cursor = db.get_cursor()

        self.__insert_into_employees(cursor)
        self.__insert_into_empoyees_and_positions(cursor)
        
        cursor.connection.commit()


    def __insert_into_empoyees_and_positions(self, cursor: Cursor):

        cursor.execute(f"""
                        SELECT id FROM employees
                        WHERE login = "{self.entry_login.get()}"
                        AND password = "{self.entry_password.get()}"
                        """)
        
        employee_id = list(cursor.fetchone())

        cursor.execute(f"""
                        SELECT id FROM job_title
                        WHERE name = "{self.stringVar_job_title.get()}"
                        """)

        job_title_id = list(cursor.fetchone())

        cursor.execute(f"""
                        SELECT id FROM department
                        WHERE name = "{self.stringVar_department.get()}"
                        """)
        
        department_id = list(cursor.fetchone())


        cursor.execute(f"""
                        INSERT INTO employees_and_positions (id_employee, id_job_title, id_department)
                        VALUES ({employee_id[0]}, {job_title_id[0]}, {department_id[0]})
                       """)


    def __insert_into_employees(self, cursor: Cursor):
        role = ''
        
        if self.stringVar_position.get() == 'Администрация':
            role = 'admin'

        elif self.stringVar_position.get() == 'Преподаватель':
            role = 'teacher'

        elif self.stringVar_position.get() == 'Технический персонал':
            role = 'staff'


        cursor.execute(f"""
                        INSERT INTO employees(name, second_name, surname, login, password,
                        role, age, date_birth, status_vacation, status_retirement,
                        status_pre_retirement, status_childless, status_many_children,
                        status_veteran)
                        VALUES ("{self.entry_name.get()}", "{self.entry_secondname.get()}",
                        "{self.entry_surnmae.get()}", "{self.entry_login.get()}",
                        "{self.entry_password.get()}", "{role}",
                        {self.entry_age.get()}, "{self.entry_date_birth.get()}",
                        "{self.stringVar_vacation.get()}", "{self.stringVar_retirement.get()}",
                        "{self.stringVar_pre_retiremen.get()}", "{self.stringVar_childless.get()}",
                        "{self.stringVar_many_children.get()}", "{self.stringVar_veteran.get()}")
                       """)

    def __back(self):

        self.quit()
        self.destroy()

        from admin_panel import Admin_panel
        Admin_panel()

    def __label_pack(self, frame: ttk.Entry) -> None:
        """
        Функция для размещения на странице лэйблов
        """

        labels = ['Имя: ', 'Фамилия: ', 'Отчество: ', 'Возраст: ', 'Департамент: ', 'Должность: ',
                  'Дата Рождения: ', 'Позиция: ', 'Ветеран: ', 'Многодетный: ', 
                  'Бездетный', 'Пенсионер: ', 'Предпенсионный возраст: ', 'В отпуске: ', 'Логин: ',
                  'Пароль: ',
                ]

        count = 0        
        for name_label in labels:
            ttk.Label(frame, text=name_label).grid(row=count, column=0)
            count += 1

    def __entry_pack(self, frame: ttk.Frame) -> None:
        """
        Функция для размещения на странице entry
        """

        from usefull_functions import DEPARTMENTS, JOB_TITLE, CHOICES_FOR_ROLE, CHOICES_FOR_STATUS

        self.entry_name: ttk.Entry = ttk.Entry(frame)
        self.entry_name.grid(row=0, column=1)

        self.entry_secondname: ttk.Entry = ttk.Entry(frame)
        self.entry_secondname.grid(row=1, column=1)

        self.entry_surnmae: ttk.Entry = ttk.Entry(frame)
        self.entry_surnmae.grid(row=2, column=1)

        self.entry_age: ttk.Entry = ttk.Entry(frame)
        self.entry_age.grid(row=3, column=1)

        self.stringVar_department = tk.StringVar(frame)
        entry_department = ttk.OptionMenu(frame, self.stringVar_department, DEPARTMENTS[0], *DEPARTMENTS)
        entry_department.grid(row=4, column=1)

        

        self.stringVar_job_title = tk.StringVar(frame)
        entry_job_title = ttk.OptionMenu(frame, self.stringVar_job_title, JOB_TITLE[0], *JOB_TITLE)
        entry_job_title.grid(row=5, column=1)

        self.entry_date_birth: ttk.Entry = ttk.Entry(frame)
        self.entry_date_birth.grid(row=6, column=1)

        self.stringVar_position = tk.StringVar(frame)
        entry_position: ttk.OptionMenu = ttk.OptionMenu(frame, self.stringVar_position, CHOICES_FOR_ROLE[0], *CHOICES_FOR_ROLE)
        entry_position.grid(row=7, column=1)

        self.stringVar_veteran = tk.StringVar(frame)
        entry_veteran: ttk.OptionMenu = ttk.OptionMenu(frame, self.stringVar_veteran, CHOICES_FOR_STATUS[0], *CHOICES_FOR_STATUS)
        entry_veteran.grid(row=8, column=1)

        self.stringVar_many_children = tk.StringVar(frame)
        entry_many_children: ttk.OptionMenu = ttk.OptionMenu(frame, self.stringVar_many_children, CHOICES_FOR_STATUS[0], *CHOICES_FOR_STATUS)
        entry_many_children.grid(row=9, column=1)

        self.stringVar_childless = tk.StringVar(frame)
        entry_childless: ttk.OptionMenu = ttk.OptionMenu(frame, self.stringVar_childless, CHOICES_FOR_STATUS[0], *CHOICES_FOR_STATUS)
        entry_childless.grid(row=10, column=1)

        self.stringVar_retirement = tk.StringVar(frame)
        entry_retirement: ttk.OptionMenu = ttk.OptionMenu(frame, self.stringVar_retirement, CHOICES_FOR_STATUS[0], *CHOICES_FOR_STATUS)
        entry_retirement.grid(row=11, column=1)

        self.stringVar_pre_retiremen = tk.StringVar(frame)
        entry_pre_retirement: ttk.OptionMenu = ttk.OptionMenu(frame, self.stringVar_pre_retiremen, CHOICES_FOR_STATUS[0], *CHOICES_FOR_STATUS)
        entry_pre_retirement.grid(row=12, column=1)

        self.stringVar_vacation = tk.StringVar(frame)
        entry_vacation: ttk.OptionMenu = ttk.OptionMenu(frame, self.stringVar_vacation, CHOICES_FOR_STATUS[0], *CHOICES_FOR_STATUS)
        entry_vacation.grid(row=13, column=1)

        self.entry_login: ttk.Entry = ttk.Entry(frame)
        self.entry_login.grid(row=14, column=1)

        self.entry_password: ttk.Entry = ttk.Entry(frame)
        self.entry_password.grid(row=15, column=1)
