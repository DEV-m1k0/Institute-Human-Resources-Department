import tkinter as tk
from check_tables import Check_all_tables


class Admin_panel(tk.Tk):
    """
    Класс панели админа для выбора действий
    """
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        
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
        admin_panel_label = tk.Label(self, text='Панель Администратора', font=('Ariel', 28))
        see_all_btn = tk.Button(self, text="Просмотреть таблицы", font=("Arial", 14), command=self.__see_all)
        register_user_btn = tk.Button(self, text="Зарегистрировать пользователя", font=("Arial", 14), command=self.__register_user)
        edit_users_data_btn = tk.Button(self, text="Отредактировать дынные пользователей", font=("Arial", 14), command=self.__edit_users_data)
        
        # Размещаем их
        admin_panel_label.pack(pady=25)
        see_all_btn.pack(pady=20)
        register_user_btn.pack(pady=20)
        edit_users_data_btn.pack(pady=20)
    
    def __see_all(self):
        """
        Функция для открытия окна для просмотра всех записей
        """
        print('tbd')
        # self.destroy()
        # Check_all_tables()
        
    
    def __register_user(self):
        """
        Функция для открытия окна для регистрации новых пользователей
        """
        from reg_user import RegistrationUsers
        RegistrationUsers()
        
        self.destroy()
    
    def __edit_users_data(self):
        """
        Функция для открытия окна для редактирования данных пользователей
        """
        print('tbd')