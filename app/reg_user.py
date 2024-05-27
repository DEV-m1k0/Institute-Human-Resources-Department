from tkinter import ttk, Tk
import tkinter as tk


class RegistrationUsers(Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.geometry('500x500')
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
        frame.pack()

        self.__label_pack(frame)
        self.__entry_pack(frame)

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
                  'Зарплата: ', 'Дата Рождения: ', 'Позиция: ', 'Ветеран: ', 'Многодетный: ', 
                  'Бездетный', 'Пенсионер: ', 'Предпенсионный возраст: ', 'В отпуске: ', 'Лонин: ',
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

        entry_name = ttk.Entry(frame).grid(row=0, column=1)
        entry_secondname = ttk.Entry(frame).grid(row=1, column=1)
        entry_surnmae = ttk.Entry(frame).grid(row=2, column=1)
        entry_age = ttk.Entry(frame).grid(row=3, column=1)
        entry_department = ttk.Entry(frame).grid(row=4, column=1)
        entry_job_title = ttk.Entry(frame).grid(row=5, column=1)
        entry_sallary = ttk.Entry(frame).grid(row=6, column=1)
        entry_date_birth = ttk.Entry(frame).grid(row=7, column=1)
        entry_position = ttk.Entry(frame).grid(row=8, column=1)
        entry_veteran = ttk.Entry(frame).grid(row=9, column=1)
        entry_many_children = ttk.Entry(frame).grid(row=10, column=1)
        entry_childless = ttk.Entry(frame).grid(row=11, column=1)
        entry_retirement = ttk.Entry(frame).grid(row=12, column=1)
        entry_pre_retirement = ttk.Entry(frame).grid(row=13, column=1)
        entry_vacation = ttk.Entry(frame).grid(row=14, column=1)
        entry_login = ttk.Entry(frame).grid(row=15, column=1)
        entry_password = ttk.Entry(frame).grid(row=16, column=1)
