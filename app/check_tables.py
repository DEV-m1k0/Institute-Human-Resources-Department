import tkinter as tk
from create_DB import CreateDataBase
from tkinter import ttk

class Check_all_tables(tk.Tk):
    """
    Класс для просмотра всех записей
    """
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        
        self.geometry("650x600")
        self.title("Tables")
        self.resizable(height=False, width=False)
        
        self.__add_widgets()
        self.mainloop()
        
        self.vacancy_sort = {"Должности":'id_job_title', 
                             "Кафедры":'id_department',
                             'Дата открытия':"vacancy_opening_date",
                             'Дата закрытия':"vacancy_closing_date"}
    
    def __add_widgets(self):
        """
        Функция для добавления виджетов на экран
        """
        
        # Список названий таблиц
        self.tables_names = {'Вакансии': ["Должности", "Кафедры", 'Дата открытия', 'Дата закрытия'],
                             'Сотрудники':["Должности", "Кафедры", "TBA"]}
        
        # Создаем виджеты
        tables_label = tk.Label(self, text='Просмотр всех записей', font=('Ariel', 28))
        self.tables_name_combobox =  ttk.Combobox(self, values=list(self.tables_names.keys()), state="readonly")
        self.tables_name_combobox.bind("<<ComboboxSelected>>", self.__selected)
        self.tables_data_listbox = tk.Listbox(self, height=20, width=100)
        self.sort_combobox = ttk.Combobox(self)
        
        # Размещаем их
        tables_label.pack()
        self.tables_name_combobox.pack()
        self.sort_combobox.pack()
        self.tables_data_listbox.pack()
    
    def __selected(self, event):
        """
        Функция выбора таблиц для просмотра
        """
        self.tables_data_listbox.delete(0, 'end')
        self.sort_combobox['values'] = self.tables_names[self.tables_name_combobox.get()]
        
        db = CreateDataBase()
        cursor = db.get_cursor()
        if self.tables_name_combobox.get() == "Вакансии":
            table_name = 'job_vacancy'
        elif self.tables_name_combobox.get() == "Сотрудники":
            table_name = 'employees_and_positions'
        cursor.execute(f"""
                       SELECT * FROM {table_name}
                       """)
        for el in cursor.fetchall():
            self.tables_data_listbox.insert(0, el)

