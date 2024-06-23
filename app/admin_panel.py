from typing import Tuple
from check_tables import Check_all_tables
import customtkinter as ctk

class Admin_panel(ctk.CTk):
    """
    Класс панели админа для выбора действий
    """
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        self.geometry("450x350")
        self.title("Admin panel")
        self.resizable(height=False, width=False)

        self.__add_widgets()
        
        self.mainloop()
    
    def __add_widgets(self):
        """
        Функция для добавления виджетов на экран
        """
        # Создаем виджеты
        admin_panel_label = ctk.CTkLabel(
            self, text="Панель Администратора", font=("Ariel", 28)
        )
        see_all_btn = ctk.CTkButton(
            self, text="Просмотреть таблицы", font=("Arial", 14), command=self.__see_all
        )
        register_user_btn = ctk.CTkButton(
            self,
            text="Зарегистрировать пользователя",
            font=("Arial", 14),
            command=self.__register_user,
        )
        add_vacancy_btn = ctk.CTkButton(
            self,
            text="Добавить вакансию",
            font=("Arial", 14),
            command=self.__add_vacancy,
        )
        import_excel = ctk.CTkButton(
            self,
            text="Импортировать из excel",
            font=("Arial", 14),
            command=self.__add_excel,
        )

        # Размещаем их
        admin_panel_label.pack(pady=25)
        see_all_btn.pack(pady=20)
        register_user_btn.pack(pady=20)
        add_vacancy_btn.pack(pady=20)
        import_excel.pack(pady=20)
        
    def __add_excel(self):
        """
        Функция для импорта пользователей через excel
        """
        from import_excel import ImportExcel

        top_level = ImportExcel()
        top_level.mainloop()
    
    def __see_all(self):
        """
        Функция для открытия окна для просмотра всех записей
        """
        self.destroy()
        
        Check_all_tables()

        
    
    def __register_user(self):
        """
        Функция для открытия окна для регистрации новых пользователей
        """
        from reg_user import RegistrationUsers
        
        self.destroy()  
        RegistrationUsers()

    
    def __add_vacancy(self):
        from add_vacancy import AddVacancy

        self.destroy()
        AddVacancy()