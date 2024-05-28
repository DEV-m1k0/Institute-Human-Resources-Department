from tkinter import Tk
from tkinter.ttk import *
from staff_sort_page import StaffAllNotes


class StaffPanel(Tk):
    """
    Панель персонала
    """

    def __init__(self, department, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.geometry('450x350')
        self.title('Staff\'s panel')

        self.department = department
        
        self.__add_widgets()

        self.mainloop()

    def __add_widgets(self) -> None:
        """
        Добавление и размещение виджетов
        """
        
        main_label = Label(self, text='Панель персонала', font='Arial 28')
        main_label.pack()

        button_all_notes = Button(self, text='Просмотреть записи', command=self.__redirect_to_all_notes)
        button_all_notes.pack()


    def __redirect_to_all_notes(self):
        """
        Переадресация на страницу с записями о сотрудниках
        """
        
        self.destroy()
        StaffAllNotes(self.department)
        


