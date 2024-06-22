import tkinter as tk
from typing import Tuple
from create_DB import get_cursor
from tkinter import ttk
import customtkinter as ctk

class Check_all_tables(ctk.CTk):
    """
    Класс для просмотра всех записей
    """
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        self.geometry("1280x400")
        self.title("Tables")
        self.resizable(height=False, width=False)
        
        # Словарь для комбобокса с фильтрациями
        self.sort_names = {"Все" : "Все", 'В отпуске' : 'status_vacation', 'Пенсионер':'status_retirement', 'Предпенсионного возраста':'status_pre_retirement', 'Бездетный':'status_childless',
                           'Многодетный':'status_many_children', 'Ветеран':'status_veteran'}
        
        self.__add_widgets()
        
        self.mainloop()        

    def item_selected_employees(self, value):

        selected_position = self.tables_data_view.selection()[0]
        selected_value = self.tables_data_view.item(selected_position, 'values')

        from editing_entries import EditEntrie
        EditEntrie(selected_value)

    def item_selected_vacany(self, value):

        selected_position = self.tables_data_view.selection()[0]
        selected_value = self.tables_data_view.item(selected_position, 'values')
        
        from edit_vacancy import EditVacancy
        EditVacancy(selected_value)
        


    def __add_widgets(self):
        """
        Функция для добавления виджетов на экран
        """
        
        # Создаем виджеты
        tables_label = ctk.CTkLabel(self, text='Просмотр всех записей', font=('Ariel', 28))
        
        self.tables_name_var = tk.StringVar(self)
        self.sort_var = tk.StringVar(self)
        self.tables_name_var.trace('w', self.__choose)
        self.sort_var.trace('w', self.__sort)
        self.tables_name_optionmenu =  ctk.CTkOptionMenu(self,values=['Вакансии','Сотрудники'], variable=self.tables_name_var)
        self.tables_name_var.set('Выберите таблицу')
        
        self.tables_data_view = ttk.Treeview(self, show='headings')
        
        self.sort_optionmenu = ctk.CTkOptionMenu(self, variable=self.sort_var, values=list(self.sort_names))
        self.sort_var.set('Выберите вид сортировки')
        self.sort_optionmenu.configure(state='disabled')
        
        back_btn = ctk.CTkButton(self, text='К панели администратора', command=self.__back_to_panel)
 
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
          
        self.cursor = get_cursor()
        

        self.sort_var.set('Выберите вид сортировки')
        
        # Проверка выбора таблицы
        if self.tables_name_var.get() == "Вакансии":

            self.tables_data_view.bind('<<TreeviewSelect>>', self.item_selected_vacany)
            
            columns = ('ID', 'Вакансия', 'Зарплата', 'Отдел', 'Дата открытия', 'Дата закрытия')           
            self.tables_data_view['columns'] = columns
            
            for i in columns:
                self.tables_data_view.heading(f'#{1+columns.index(i)}', text=i)
            self.tables_data_view.column("#1", width=40, stretch='NO')
            self.tables_data_view.column("#3", width=70, stretch='NO')
    
            self.sort_optionmenu.configure(state='disabled')
            
            queue = """
                       SELECT job_vacancy.id, job_title.name, job_title.salary, department.name, vacancy_opening_date, vacancy_closing_date FROM job_vacancy
                       inner join job_title on job_vacancy.id_job_title = job_title.id
                       inner join department on department.id = job_vacancy.id_department
                       """
                       
        elif self.tables_name_var.get() == "Сотрудники":
            #💀
            self.tables_data_view.bind('<<TreeviewSelect>>', self.item_selected_employees)

            columns = ('ID', 'Вакансия', 'Отдел', 'Имя', 'Фамиля', 'Отчество', 'Логин', 'Пароль', 'Роль', 'Возраст', 'Дата_рождения',
                       'Отпуск', 'Пенсионер', 'Предпенсионер', 'Бездетный', 'Многодетный', 'Ветеран')           
            self.tables_data_view['columns'] = columns   
            
            for i in columns:
                self.tables_data_view.heading(f'#{1+columns.index(i)}', text=i)
                
            self.tables_data_view.column("#1", width=40, stretch='NO')


                
            self.sort_optionmenu.configure(state='enabled')
            
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
        if self.sort_names[self.sort_var.get()] == 'Все':
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
        else:
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
    
