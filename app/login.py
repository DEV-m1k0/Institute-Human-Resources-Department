import tkinter as tk


class Login(tk.Tk):
    """
    Класс для страницы со входом в систему
    """

    def __init__(
        self,
        screenName: str | None = None,
        baseName: str | None = None,
        className: str = "Tk",
        useTk: bool = True,
        sync: bool = False,
        use: str | None = None,
    ) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.geometry("600x600")
        self.title("Login")

        self.mainloop()
