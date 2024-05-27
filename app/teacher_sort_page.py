from tkinter import Tk, LEFT
from tkinter.ttk import *
from create_DB import CreateDataBase
import usefull_functions as uf

class TeacherAllNotes(Tk):
    """
    Страница с записями\n
    \nВозможности сортировки:
    1) Предпенсионный возраст\n
    2) Юбиляры текущего года\n
    3) Бездетные сотрудники\n
    4) Многодетные сотрудники\n
    5) Ветераны
"""

    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.geometry("650x600")
        self.title('Notes')

        self.notes = ['Сортировка сотрудников', 'Предпенсионный возраст', 'Юбиляры', 'Бездетные', 'Многодетные', 'Ветераны']
        self.rows: dict[Label] = []

        self.__add_widgets()

        db = CreateDataBase()
        self.cursor = db.get_cursor()

        self.mainloop()


    def __add_widgets(self):
        """
        Добавление и размещение виджетов
        """

        self.sorting = Combobox(self, values=self.notes)
        self.sorting.current(0)
        self.sorting.pack()

        self.place = Frame(self)
        self.place.pack()

        label_name = Label(self.place, text='Имя')
        label_name.grid(row=0, column=1)

        label_secondname = Label(self.place, text='Фамилия')
        label_secondname.grid(row=0, column=2)

        label_surname = Label(self.place, text='Отчество')
        label_surname.grid(row=0, column=3)

        label_login = Label(self.place, text='Роль')
        label_login.grid(row=0, column=4)

        label_login = Label(self.place, text='Возраст')
        label_login.grid(row=0, column=5)

        label_date_birth = Label(self.place, text='День родения')
        label_date_birth.grid(row=0, column=6)

        self.place.rowconfigure(0, minsize=50)

        for i in range(7):
            self.place.columnconfigure(index=i+1, minsize=100)

        self.sorting.bind('<<ComboboxSelected>>', self.__set_value)

    def __printing_notes(self) -> None:
        count = 0

        if len(self.accepted_notes) != 0:
            for user in self.accepted_notes:
                count += 1
                _, name, secondname, surname, _, _, role, age, birth, _, _, _, _, _, _ = user
                user_data = [name, secondname, surname, role, age, birth]
                for index in range(len(user_data)):
                    Label(self.place, text=f"{count}").grid(row=count, column=0)
                    # self.rows.append(Label(self.place, text=user_data[index]))
                    # self.__set_widgets(self.rows, count)
                    Label(self.place, text=user_data[index]).grid(row=1, column=index+1)

        else:
            print(self.rows)

    def __set_widgets(self, rows: dict[Label], count_rows: int):
        for row in rows:
            for i in range(len(row)):
                row.grid(row='') #TODO(Надо доработать расположение записей во Frame)
            

    def __set_value(self, event) -> None:
        note = self.sorting.get()
        if note == "Сортировка сотрудников":
            pass

        else:
            self.accepted_notes = uf.sorting_users_by_status_pre_retirment(note)
            self.__printing_notes()
            