from typing import Tuple
import customtkinter as ctk
from create_DB import get_cursor
from sqlite3 import Cursor
import tkinter as tk

class AddVacancy(ctk.CTk):
    """
    Класс с окном добавления вакансии
    """

    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.geometry('500x300')
        self.resizable(width=False, height=False)
        self.title('Add vacancy')

        self.__add_widgets()
        self.mainloop()

    def __add_widgets(self):
        """
        Функция для добавления виджетов
        """

        ctk.CTkButton(self, text='<- Назад', command=self.__back).pack(pady=10)

        main_title_label = ctk.CTkLabel(self, text="Добавление вакансий", font=("Arial", 28))
        main_title_label.pack()

        frame = ctk.CTkFrame(self)
        frame.pack(pady=20)

        self.complete_label = ctk.CTkLabel(self, text='')
        self.complete_label.pack()

        self.__label_pack(frame)
        self.__entry_pack(frame)

        ctk.CTkButton(self, text='Зарегестрировать', command=self.__reg).pack()

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
        self.complete_label.configure(text='Вакансия успешно добавлена', fg_color='Green')


    def __back(self):

        self.quit()
        self.destroy()

        from admin_panel import Admin_panel
        Admin_panel()

    def __label_pack(self, frame: ctk.CTkEntry) -> None:
        """
        Функция для размещения на странице лэйблов
        """

        labels = ['Должность: ', 'Отдел: ', 'Дата открытия вакансии: ', 'Дата закрытия вакансии: ']

        count = 0        
        for name_label in labels:
            ctk.CTkLabel(frame, text=name_label).grid(row=count, column=0)
            count += 1

    def __entry_pack(self, frame: ctk.CTkFrame) -> None:
        """
        Функция для размещения на странице entry
        """

        from usefull_functions import DEPARTMENTS, JOB_TITLE, CHOICES_FOR_ROLE, CHOICES_FOR_STATUS

        self.StringVar_job_title = tk.StringVar(frame)
        job_title = ctk.CTkOptionMenu(frame, variable=self.StringVar_job_title, values=JOB_TITLE)
        job_title.set(JOB_TITLE[0])
        job_title.grid(row=0, column=1)

        self.StringVar_department = tk.StringVar(frame)
        department = ctk.CTkOptionMenu(frame, variable=self.StringVar_department, values=DEPARTMENTS)
        department.set(DEPARTMENTS[0])
        department.grid(row=1, column=1)

        self.date_opening = ctk.CTkEntry(frame)
        self.date_opening.grid(row=2, column=1)
        
        self.date_closing = ctk.CTkEntry(frame)
        self.date_closing.grid(row=3, column=1)
        
