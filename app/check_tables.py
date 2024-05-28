import tkinter as tk
from create_DB import CreateDataBase
from tkinter import ttk


class Check_all_tables(tk.Tk):
    """
    Класс для просмотра всех записей
    """
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        
        self.geometry("1280x500")
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
        self.sort_var = tk.StringVar(self)
        self.tables_name_var.trace('w', self.__choose)
        self.sort_var.trace('w', self.__sort)
        self.tables_name_optionmenu =  ttk.OptionMenu(self, self.tables_name_var, 'Выберите таблицу', *('Вакансии','Сотрудники'))
        
        self.tables_data_view = ttk.Treeview(self, show='headings')
        

        self.sort_optionmenu = ttk.OptionMenu(self, self.sort_var, 'Выберите вид сортировки', *self.sort_names)
        self.sort_optionmenu['state'] = 'disabled'
        
        back_btn = tk.Button(self, text='К панели администратора', command=self.__back_to_panel)
 
        # Размещаем их
        tables_label.pack()
        self.tables_name_optionmenu.pack()
        self.sort_optionmenu.pack()
        self.tables_data_view.pack()
        back_btn.pack()
    
    def __choose(self, *args):
        """
        Функция выбора таблиц для просмотра
        """
        for i in self.tables_data_view.get_children():
            self.tables_data_view.delete(i)
          
        self.db = CreateDataBase()
        self.cursor = self.db.get_cursor()
        
        self.sort_var.set('Выберите вид сортировки')
        
        # Проверка выбора таблицы
        if self.tables_name_var.get() == "Вакансии":
            
            columns = ('ID', 'Вакансия', 'Зарплата', 'Отдел', 'Дата открытия', 'Дата закрытия')           
            self.tables_data_view['columns'] = columns   
            
            for i in columns:
                self.tables_data_view.heading(f'#{1+columns.index(i)}', text=i)       
            self.tables_data_view.column("#1", width=40, stretch='NO')
            self.tables_data_view.column("#3", width=70, stretch='NO')
    
            self.sort_optionmenu['state'] = 'disabled'
            
            queue = """
                       SELECT job_vacancy.id, job_title.name, job_title.salary, department.name, vacancy_opening_date, vacancy_closing_date FROM job_vacancy
                       inner join job_title on job_vacancy.id_job_title = job_title.id
                       inner join department on department.id = job_vacancy.id_department
                       """
                       
        elif self.tables_name_var.get() == "Сотрудники":
            #💀
            columns = ('ID', 'Вакансия', 'Отдел', 'Имя', 'Фамиля', 'Отчество', 'Логин', 'Пароль', 'Роль', 'Возраст', 'Дата_рождения',
                       'Отпуск', 'Пенсионер', 'Предпенсионер', 'Бездетный', 'Многодетный', 'Ветеран')           
            self.tables_data_view['columns'] = columns   
            
            for i in columns:
                self.tables_data_view.heading(f'#{1+columns.index(i)}', text=i)
                
            self.tables_data_view.column("#1", width=40, stretch='NO')

                
            self.sort_optionmenu['state'] = 'enabled'
            
            queue = """
                       SELECT employees_and_positions.id, job_title.name,department.name, employees.name, employees.second_name, employees.surname,
                        employees.login, employees.password, employees.role, employees.age, employees.date_birth, 
                        employees.status_vacation, employees.status_retirement, employees.status_pre_retirement, 
                        employees.status_childless, employees.status_many_children, employees.status_veteran
                       FROM employees_and_positions
                       inner join job_title on employees_and_positions.id_job_title = job_title.id
                       inner join department on department.id = employees_and_positions.id_department
                       inner join employees on employees_and_positions.id_employee = employees.id

                       """
            self.sort_optionmenu['state'] = 'enabled'
        self.cursor.execute(queue)
        
        for el in self.cursor.fetchall():
            self.tables_data_view.insert("",tk.END, values=el)
    
    def __sort(self, *args):
        """
        Функция выбора фильтрации для таблиц
        """
        for i in self.tables_data_view.get_children():
            self.tables_data_view.delete(i)
        
        columns = ('ID', 'Вакансия', 'Отдел', 'Имя', 'Фамиля', 'Отчество', 'Логин', 'Пароль', 'Роль', 'Возраст', 'Дата_рождения',
                       'Отпуск', 'Пенсионер', 'Предпенсионер', 'Бездетный', 'Многодетный', 'Ветеран')           
        self.tables_data_view['columns'] = columns   
            
        for i in columns:
            self.tables_data_view.heading(f'#{1+columns.index(i)}', text=i)
                
        self.tables_data_view.column("#1", width=40, stretch='NO')
            
        queue = f"""
                       SELECT employees_and_positions.id, job_title.name,department.name, employees.name, employees.second_name, employees.surname,
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
            self.tables_data_view.insert("",tk.END, values=el)
    
    def __back_to_panel(self):
        """
        Функция для возврата в панель
        """
        self.destroy()
        
        from admin_panel import Admin_panel
        Admin_panel()
        

