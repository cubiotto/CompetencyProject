import customtkinter
from customtkinter import CTkLabel
import tkinter
from Styles.styles import title_font, h1_font, button_font
from Windows.components import InputSection

class TopLevelCompetencySettings(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry("800x800")
        self.title("Competency Settings")
        self.columnconfigure(0, weight=1)
        self.label = customtkinter.CTkLabel(self, text="Competency Settings", font=title_font, padx=5, pady=5)
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="nwe")

        # Input Category field
        self.category_frame = InputSection(self, "Category")
        self.category_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nw")

        # self.category_label = CTkLabel(self.category_frame, text="Category", font=h1_font, padx=5, pady=5)
        # self.category_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
        #
        # self.category_input = customtkinter.CTkEntry(self.category_frame, width=220, height=50)
        # self.category_input.grid(row=1, column=0, padx=(10, 0), sticky="nw")
        #
        # self.category_add_btn = customtkinter.CTkButton(self.category_frame, text="Add", font=button_font, height=50, width=50, command=self.category_add_btn)
        #
        # self.category_add_btn.grid(row=1, column=1, padx=10, sticky="n")


        self.category_list_frame = customtkinter.CTkScrollableFrame(self.category_frame, height=300, width=200)
        self.category_list_frame.grid(row=2, column=0, padx=10, pady=10)

        self.category_list = []

    def category_add_btn(self, category_list=None):
        category_data = self.category_input.get()
        self.category_list.append(category_data)
        self.category_input.delete(0, "end")