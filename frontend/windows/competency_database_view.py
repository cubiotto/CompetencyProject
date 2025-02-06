from pathlib import Path
from tkinter import messagebox

import customtkinter
import tkinter
import os

from backend.core.DatabaseConnection import DatabaseConnection
from backend.models.Category import Category
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

        # Initialize database connection
        self.db_path = (
            Path(__file__).parent  # frontend/windows
            .parent.parent  # CompetencyProject
            / "backend"
            / "database"
            / "CompetencyDatabase.db"
        )
        self.db_conn = DatabaseConnection(self.db_path)

        # GUI Components
        self.input_label = customtkinter.CTkLabel(self, text="Input Database", font=h1_font)
        self.input_label.grid(row=1, column=0, padx=10, pady=10, sticky="nw")

        # Input Section
        self.input_frame = customtkinter.CTkFrame(self, fg_color="gray", corner_radius=20, height=50)
        self.input_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nwe")

        # Input fields
        self.input_field = InputField(
            self.input_frame,
            "Category Database",
            "Input Category",
            command=self.handle_add_category
        )
        self.input_field.grid(row=2, column=0, padx=10, pady=10, sticky="nw")

        # Category List Display
        self.category_list_frame = customtkinter.CTkFrame(self, fg_color="gray", corner_radius=10, height=400, width=400)
        self.category_list_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nw")
        self.category_list_frame.grid_propagate(False)

        # Initial population of categories
        self.refresh_category_list()

    def handle_add_category(self, category_name):
        """Add a new category to the database and refresh the list."""
        try:
            # Create and save the category
            new_category = Category(self.db_conn, category_name=category_name)
            new_category.save_category()
            # Clear Input Field
            self.input_field.category_input.delete(0, "end")
            # Refresh the displayed list
            self.refresh_category_list()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add category: {str(e)}")

    def refresh_category_list(self):
        """Update the displayed list of categories."""
        # Clear existing labels
        for widget in self.category_list_frame.winfo_children():
            widget.destroy()

        # Fetch categories from the database
        categories = Category.fetch_all(self.db_conn)

        # Repopulate the list
        for idx, category in enumerate(categories):
            label = customtkinter.CTkLabel(
                self.category_list_frame,
                text=category.category_name,
                font=h1_font
            )
            label.grid(row=idx, column=0, padx=10, pady=5, sticky="w")