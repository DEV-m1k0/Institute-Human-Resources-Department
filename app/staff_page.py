from typing import Tuple
import customtkinter as ctk
from staff_sort_page import StaffAllNotes


class StaffPanel(ctk.CTk):
    """
    Панель персонала
    """

    def __init__(self, fg_color: str | Tuple[str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.geometry('450x350')
        self.title('Staff\'s panel')
        self.resizable(height=False, width=False)

        
        self.__add_widgets()

        self.mainloop()

    def __add_widgets(self) -> None:
        """
        Добавление и размещение виджетов
        """
        
        main_label = ctk.CTkLabel(self, text='Панель персонала', font=("Arial", 28))
        main_label.pack()

        button_all_notes = ctk.CTkButton(self, text='Просмотреть записи', command=self.__redirect_to_all_notes)
        button_all_notes.pack()


    def __redirect_to_all_notes(self):
        """
        Переадресация на страницу с записями о сотрудниках
        """
        
        self.destroy()
        StaffAllNotes()
        


