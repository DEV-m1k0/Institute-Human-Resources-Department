import tkinter as tk
from tkinter import ttk
from create_DB import CreateDataBase


class StaffAllNotes(tk.Tk):
    """
    Страница с записями\n
    \nВозможности сортировки:
    1) Предпенсионный возраст\n
    2) Юбиляры текущего года\n
    3) Бездетные сотрудники\n
    4) Многодетные сотрудники\n
    5) Ветераны
"""

    def __init__(self, department, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.geometry("650x300")
        self.title('Notes')
        self.resizable(height=False, width=False)
        
        self.department = department       
        
        self.sort_names = {"Все" : "Все", 'В отпуске' : 'status_vacation', 'Пенсионер':'status_retirement', 'Предпенсионного возраста':'status_pre_retirement', 'Бездетный':'status_childless',
                           'Многодетный':'status_many_children', 'Ветеран':'status_veteran'}

        
        self.__add_widgets()
        self.__fill()


       
        self.mainloop()


    def __add_widgets(self):
        """
        Добавление и размещение виджетов
        """

        # Создаем виджеты
        self.sort_var = tk.StringVar(self)
        self.sort_var.trace('w', self.__sort)
        self.sort_optionmenu =  ttk.OptionMenu(self, self.sort_var, 'Выбирите сортировку', *self.sort_names)
        back_button = tk.Button(self, text='К панели персонала', command=self.__back_to_panel)
        self.tables_data_view = ttk.Treeview(self, show='headings')

        # Размещаем их
        self.sort_optionmenu.pack()
        self.tables_data_view.pack()
        back_button.pack()
        
        

    def __fill(self, *args):
        """
        Функция для заполнения таблицы
        """
        
        db = CreateDataBase()
        self.cursor = db.get_cursor()
        
        columns = ('ID', 'Имя', 'Фамилия', 'Отчество', 'Роль','Отдел','Дата рождения')           
        self.tables_data_view['columns'] = columns   
            
        for i in columns:
            self.tables_data_view.heading(f'#{1+columns.index(i)}', text=i)
            self.tables_data_view.column(f'#{1+columns.index(i)}', width=100, stretch='NO')                    
        self.tables_data_view.column("#1", width=40, stretch='NO')      
        
        queue = f"""
                       SELECT employees.id, employees.name, employees.second_name, employees.surname, employees.role,department.name, employees.date_birth
                       FROM employees
                       inner join employees_and_positions on employees.id = employees_and_positions.id_employee  
                       inner join department on department.id = employees_and_positions.id_department
                       where employees_and_positions.id_department = {self.department}         
                       """
        self.cursor.execute(queue)
        
        for el in self.cursor.fetchall():
            self.tables_data_view.insert("",tk.END, values=el)
    
    def __sort(self, *args):
        """
        Функция выбора фильтрации для таблиц
        """
        if self.sort_names[self.sort_var.get()] == 'Все':
            queue = f"""
                       SELECT employees.id, employees.name, employees.second_name, employees.surname, employees.role,department.name, employees.date_birth
                       FROM employees
                       inner join employees_and_positions on employees.id = employees_and_positions.id_employee  
                       inner join department on department.id = employees_and_positions.id_department
                       where employees_and_positions.id_department = {self.department}       
 
                       """
        else:  
            queue = f"""
                       SELECT employees.id, employees.name, employees.second_name, employees.surname, employees.role,department.name, employees.date_birth
                       FROM employees
                       inner join employees_and_positions on employees.id = employees_and_positions.id_employee  
                       inner join department on department.id = employees_and_positions.id_department
                       where employees_and_positions.id_department = {self.department}  and {self.sort_names[self.sort_var.get()]} = "да"    
                       """
        self.cursor.execute(queue)
        
        for i in self.tables_data_view.get_children():
            self.tables_data_view.delete(i)
            
        for el in self.cursor.fetchall():
            self.tables_data_view.insert("",tk.END, values=el)
    
    def __back_to_panel(self):
        """
        Функция для возврата в панель
        """
        self.destroy()
        
        from staff_page import StaffPanel
        StaffPanel(self.department)

