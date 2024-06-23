from typing import Tuple
import customtkinter as ctk
from teacher_sort_page import TeacherAllNotes


class TeacherPanel(ctk.CTk):
    """
    Панель преподавателя
    """

    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.geometry('450x350')
        self.title('Teacher\'s panel')
        self.resizable(height=False, width=False)
        

        self.__add_widgets()

        self.mainloop()

    def __add_widgets(self) -> None:
        """
        Добавление и размещение виджетов
        """
        # Создаем виджеты
        main_label = ctk.CTkLabel(self, text='Панель преподавателя', font=('Arial', 28))
        button_all_notes = ctk.CTkButton(self, text='Просмотреть записи', command=self.__redirect_to_all_notes)
        
        # Размещаем их
        main_label.pack()
        button_all_notes.pack()


    def __redirect_to_all_notes(self):
        """
        Переадресация на страицу с записями о сотрудниках
        """

        self.destroy()
        TeacherAllNotes()
    
