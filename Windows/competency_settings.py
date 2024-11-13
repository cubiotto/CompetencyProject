import customtkinter
from customtkinter import CTkLabel
import tkinter
from Styles.styles import title_font, h1_font, button_font
from Windows.components import SettingsInputSection

class TopLevelCompetencySettings(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry("800x800")
        self.title("Competency Settings")
        self.columnconfigure(0, weight=1)
        self.label = customtkinter.CTkLabel(self, text="Competency Settings", font=title_font, padx=5, pady=5)
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="nwe")

        # Input Category field
        self.category_frame = SettingsInputSection(self, "Category")
        self.category_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nw")
