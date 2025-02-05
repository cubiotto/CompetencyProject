from pathlib import Path

import customtkinter
import tkinter
import os

from backend.core.database_connection import DatabaseConnection
from frontend.styles.fonts import title_font, h1_font
from frontend.components.InputField import InputField


class TopLevelCompetencyDatabase(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry("800x800")
        self.title("Competency Database")
        self.columnconfigure(0, weight=1)
        self.label = customtkinter.CTkLabel(self, text="Competency Database", font=title_font)
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="nwe")

        # Setup place to input
        self.input_label = customtkinter.CTkLabel(self, text="Input Database", font=h1_font)
        self.input_label.grid(row=1, column=0, padx=10, pady=10, sticky="nw")
        self.input_frame = customtkinter.CTkFrame(self, fg_color="gray", corner_radius=50, height=50)
        self.input_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nwe")

        # Input fields
        self.db_path = (
            Path(__file__).parent  # frontend/windows
            .parent.parent  # CompetencyProject
            / "backend"
            / "database"
            / "CompetencyDatabase.db"
        )
        print(self.db_path)
        self.db_handler = DatabaseConnection(self.db_path)
        self.input_field = InputField(self.input_frame, "Category Database", "Input Category", self.db_handler)
        self.input_field.grid(row=2, column=0, padx=10, pady=10, sticky="nw")



