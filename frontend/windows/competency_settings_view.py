import customtkinter
from frontend.styles.fonts import title_font
from frontend.components.InputField import InputField

class TopLevelCompetencySettings(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry("800x800")
        self.title("Competency Settings")
        self.columnconfigure(0, weight=1)
        self.label = customtkinter.CTkLabel(self, text="Competency Settings", font=title_font, padx=5, pady=5)
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="nwe")

        # Input Category field
        self.category_frame = InputField(self, "Category")
        self.category_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nw")
