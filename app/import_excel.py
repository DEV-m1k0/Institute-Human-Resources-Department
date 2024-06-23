import customtkinter as ctk
from typing import Union, Optional, Tuple
import pandas as pd
from create_DB import get_cursor

class ImportExcel(ctk.CTkToplevel):
    def __init__(
        self, *args, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kwargs
    ):
        super().__init__(*args, fg_color=fg_color, **kwargs)

        back_button = ctk.CTkButton(self, text="<- назад", command=self.__back)
        back_button.pack()

        ctk.CTkLabel(
            self, text="Добавление пользователей через Excel", font=("Arial", 28)
        ).pack(pady=20, padx=10)

        import_button = ctk.CTkButton(
            self, text="Импортировать", command=self.import_file, width=100, height=50
        )
        import_button.pack(pady=10)
        
        

    def __back(self):
        self.destroy()

    def import_file(self):
        file_path = ctk.filedialog.askopenfilename(filetypes=[("Excel file", "*.xlsx")])

        if file_path:
            self.__read_tables(file_path)

    def __read_tables(self, file_path: str):
        try:
            df = pd.read_excel(file_path)
            self.items = df.values.tolist()
            
            

        except Exception as error:
            print(error)
            return error
        else:
            self.__insert_into_tables()
    
    def __insert_into_tables(self):
        cursor = get_cursor()
        
        for el in self.items:
            cursor.execute(f"""insert into employees(name, second_name, surname, login, password, role, age, date_birth, 
                           status_vacation, status_retirement, status_pre_retirement, status_childless, status_many_children, status_veteran)
                       values("{el[0]}", "{el[1]}", "{el[2]}", "{el[3]}", "{el[4]}", "{el[5]}", {el[6]}, "{str(el[7]).split()[0]}",
                              "{el[8]}", "{el[9]}", "{el[10]}", "{el[11]}", "{el[12]}", "{el[13]}")""")
            cursor.connection.commit()
            


        
        
        

