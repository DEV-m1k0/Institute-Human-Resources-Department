from tkinter import Tk
from tkinter.ttk import *
from teacher_sort_page import TeacherAllNotes


class TeacherPanel(Tk):
    """
    Панель преподавателя
    """

    def __init__(self, department, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.geometry('450x350')
        self.title('Teacher\'s panel')
        self.resizable(height=False, width=False)
        
        self.department = department
        
        self.__add_widgets()

        self.mainloop()

    def __add_widgets(self) -> None:
        """
        Добавление и размещение виджетов
        """
        
        # Создаем виджеты
        main_label = Label(self, text='Панель преподавателя', font='Arial 28')
        button_all_notes = Button(self, text='Просмотреть записи', command=self.__redirect_to_all_notes)
        
        # Размещаем их
        main_label.pack()
        button_all_notes.pack()


    def __redirect_to_all_notes(self):
        """
        Переадресация на страицу с записями о сотрудниках
        """

        self.destroy()
        TeacherAllNotes(self.department)
    
    


