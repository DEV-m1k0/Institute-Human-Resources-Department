import customtkinter as ctk
from typing import Union, Optional, Tuple
import pandas as pd


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

            # АРТЕЕЕЕЕЕММММ!!!! В items ЛЕЖАТ ДАННЫЕ ИЗ EXCEL. ЭТО МЕСТО ВОТ ТУТ!!!!
            items = df.values.tolist()
            print(items)

        except Exception as error:
            print(error)
            return error
