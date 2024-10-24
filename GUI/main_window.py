import customtkinter
from styles import button_font, title_font
from plugins import TopLevelCompetencyDatabase


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1080x1200')
        self.title("Competency Evaluation")

        # Row & Column Configure
        # self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.welcome_text = customtkinter.CTkLabel(self, text="Welcome to Competency Evaluation!", font=title_font)
        self.welcome_text.grid(column=0, row=0, columnspan=2, padx=10, pady=10, sticky="nwe")

        self.competency_database_btn = customtkinter.CTkButton(self, text="Competency Database", font=button_font,
                                                               command=self.open_toplevel_competency_database)
        self.competency_database_btn.grid(row=1, column=0, padx=10, pady=10, sticky="nw")

        self.toplevel_competency_database = None

    def open_toplevel_competency_database(self):
        if self.toplevel_competency_database is None or not self.toplevel_competency_database.winfo_exists():
            self.toplevel_competency_database = TopLevelCompetencyDatabase()
        else:
            self.toplevel_competency_database.focus()


competencyApp = App()
competencyApp.mainloop()
