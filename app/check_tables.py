import tkinter as tk
from create_DB import CreateDataBase
from tkinter import ttk


class Check_all_tables(tk.Tk):
    """
    Класс для просмотра всех записей
    """
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        
        self.geometry("650x450")
        self.title("Tables")
        self.resizable(height=False, width=False)
        
        # Словарь для комбобокса с фильтрациями
        self.sort_names = {'В отпуске' : 'status_vacation', 'Пенсионер':'status_retirement', 'Предпенсионного возраста':'status_pre_retirement', 'Бездетный':'status_childless',
                           'Многодетный':'status_many_children', 'Ветеран':'status_veteran'}
        
        self.__add_widgets()
        
        self.mainloop()        
    
    def __add_widgets(self):
        """
        Функция для добавления виджетов на экран
        """
        
        # Создаем виджеты
        tables_label = tk.Label(self, text='Просмотр всех записей', font=('Ariel', 28))
        
        self.tables_name_var = tk.StringVar(self)
        self.tables_name_var.trace('w', self.__choose)
        self.tables_name_optionmenu =  ttk.OptionMenu(self, self.tables_name_var, 'Выберите таблицу', *('Вакансии','Сотрудники'))
        
        self.tables_data_listbox = tk.Listbox(self, height=20, width=100)
        
        self.sort_var = tk.StringVar(self)
        self.sort_var.trace('w', self.__sort)
        self.sort_optionmenu = ttk.OptionMenu(self, self.sort_var, 'Выберите вид сортировки', *self.sort_names)
        self.sort_optionmenu['state'] = 'disabled'
        
        back_btn = tk.Button(self, text='К панели администратора', command=self.__back_to_panel)

        
        # Размещаем их
        tables_label.pack()
        self.tables_name_optionmenu.pack()
        self.sort_optionmenu.pack()
        self.tables_data_listbox.pack()
        back_btn.pack()
    
    def __choose(self, *args):
        """
        Функция выбора таблиц для просмотра
        """
        self.tables_data_listbox.delete(0, 'end')
        self.db = CreateDataBase()
        self.cursor = self.db.get_cursor()
        self.sort_var.set('Выберите вид сортировки')
        if self.tables_name_var.get() == "Вакансии":
            self.sort_optionmenu['state'] = 'disabled'
            
            queue = """
                       SELECT job_vacancy.id, job_title.name, job_title.salary, department.name, vacancy_opening_date, vacancy_closing_date FROM job_vacancy
                       inner join job_title on job_vacancy.id_job_title = job_title.id
                       inner join department on department.id = job_vacancy.id_department
                       order by job_vacancy.id desc
                       """
        elif self.tables_name_var.get() == "Сотрудники":
            #💀
            self.sort_optionmenu['state'] = 'enabled'
            queue = """
                       SELECT employees_and_positions.id, job_title.name, employees.name, employees.second_name, employees.surname,
                        employees.login, employees.password, employees.role, employees.age, employees.date_birth, 
                        employees.status_vacation, employees.status_retirement, employees.status_pre_retirement, 
                        employees.status_childless, employees.status_many_children, employees.status_veteran
                       FROM employees_and_positions
                       inner join job_title on employees_and_positions.id_job_title = job_title.id
                       inner join department on department.id = employees_and_positions.id_department
                       inner join employees on employees_and_positions.id_employee = employees.id
                       order by employees_and_positions.id desc
                       """
            self.sort_optionmenu['state'] = 'enabled'
        self.cursor.execute(queue)
        for el in self.cursor.fetchall():
            self.tables_data_listbox.insert(0, el)
    
    def __sort(self, *args):
        """
        Функция выбора фильтрации для таблиц
        """
        self.tables_data_listbox.delete(0, 'end')
        queue = f"""
                       SELECT employees_and_positions.id, job_title.name, employees.name, employees.second_name, employees.surname,
                        employees.login, employees.password, employees.role, employees.age, employees.date_birth, 
                        employees.status_vacation, employees.status_retirement, employees.status_pre_retirement, 
                        employees.status_childless, employees.status_many_children, employees.status_veteran
                       FROM employees_and_positions
                       inner join job_title on employees_and_positions.id_job_title = job_title.id
                       inner join department on department.id = employees_and_positions.id_department
                       inner join employees on employees_and_positions.id_employee = employees.id
                       where {self.sort_names[self.sort_var.get()]} = "да"
                       order by employees_and_positions.id desc        
                       """
        self.cursor.execute(queue)
        for el in self.cursor.fetchall():
            self.tables_data_listbox.insert(0, el)
    
    def __back_to_panel(self):
        self.destroy()
        from admin_panel import Admin_panel
        Admin_panel()
        

