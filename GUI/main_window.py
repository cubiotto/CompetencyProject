import tkinter

import customtkinter
from styles import button_font, title_font


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1080x1200')
        self.title("Competency Evaluation")

        # Row & Column Configure
        # self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        welcome_text = customtkinter.CTkLabel(self, text="Welcome to Competency Evaluation!", font=title_font)
        welcome_text.grid(column=0, row=0, columnspan=2, padx=10, pady=10, sticky="nwe")

        competency_database_btn = customtkinter.CTkButton(self, text="Competency Database", font=button_font)
        competency_database_btn.grid(row=1, column=0, padx=10, pady=10, sticky="nw")


competencyApp = App()
competencyApp.mainloop()
