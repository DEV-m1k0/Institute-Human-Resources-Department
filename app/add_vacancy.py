from tkinter import ttk, Tk
import tkinter as tk
from create_DB import get_cursor
from sqlite3 import Cursor

class AddVacancy(Tk):
    """
    Класс с окном добавления вакансии
    """

    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.geometry('500x300')
        self.resizable(width=False, height=False)
        self.title('Add vacancy')

        self.__add_widgets()

    def __add_widgets(self):
        """
        Функция для добавления виджетов
        """

        ttk.Button(self, text='<- Назад', command=self.__back).pack(pady=10)

        main_title_label = ttk.Label(self, text="Добавление вакансий", font="Arial 28")
        main_title_label.pack()

        frame = ttk.Frame(self)
        frame.pack(pady=20)

        self.complete_label = tk.Label(self, fg='Green')
        self.complete_label.pack()

        self.__label_pack(frame)
        self.__entry_pack(frame)

        ttk.Button(self, text='Зарегестрировать', command=self.__reg).pack()

    def __reg(self):
        """
        Добавление вакансии
        """

        cursor = get_cursor()

        self.__insert_vacancy(cursor)
        
        cursor.connection.commit()


    def __insert_vacancy(self, cursor: Cursor) -> None:
        """
        Добавление вакансий в базу данных
        """

        cursor.execute(f"""
                        SELECT id FROM job_title
                        WHERE name = "{self.StringVar_job_title.get()}"
                        """)
        
        job_title = list(cursor.fetchone())

        cursor.execute(f"""
                        SELECT id FROM department
                        WHERE name = "{self.StringVar_department.get()}"
                        """)
        
        department = list(cursor.fetchone())

        cursor.execute(f"""
                        INSERT INTO job_vacancy(id_job_title, id_department, vacancy_opening_date, vacancy_closing_date)
                        VALUES ("{job_title[0]}", "{department[0]}", "{self.date_opening.get()}", "{self.date_closing.get()}")
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

        labels = ['Должность: ', 'Отдел: ', 'Дата открытия вакансии: ', 'Дата закрытия вакансии: ']

        count = 0        
        for name_label in labels:
            ttk.Label(frame, text=name_label).grid(row=count, column=0)
            count += 1

    def __entry_pack(self, frame: ttk.Frame) -> None:
        """
        Функция для размещения на странице entry
        """

        from usefull_functions import DEPARTMENTS, JOB_TITLE, CHOICES_FOR_ROLE, CHOICES_FOR_STATUS

        self.StringVar_job_title = tk.StringVar(frame)
        job_title = ttk.OptionMenu(frame, self.StringVar_job_title, JOB_TITLE[0], *JOB_TITLE)
        job_title.grid(row=0, column=1)

        self.StringVar_department = tk.StringVar(frame)
        department = ttk.OptionMenu(frame, self.StringVar_department, DEPARTMENTS[0], *DEPARTMENTS)
        department.grid(row=1, column=1)

        self.date_opening = ttk.Entry(frame)
        self.date_opening.grid(row=2, column=1)
        
        self.date_closing = ttk.Entry(frame)
        self.date_closing.grid(row=3, column=1)