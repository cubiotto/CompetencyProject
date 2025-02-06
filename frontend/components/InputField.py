import sqlite3
from tkinter import messagebox

import customtkinter

from frontend.styles.fonts import h1_font, button_font
from customtkinter import CTkLabel


class InputField(customtkinter.CTkFrame):
    def __init__(self, master, input_field_name, placeholder_name, command=None):
        super().__init__(master, fg_color="transparent", corner_radius=20)
        self.input_field_name = input_field_name
        self.placeholder_name = placeholder_name
        self.command = command
        self.category_label = CTkLabel(self, text=input_field_name, font=h1_font, padx=5, pady=5, corner_radius=50)
        self.category_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.category_input = customtkinter.CTkEntry(self, width=220, height=50, corner_radius=50)
        self.category_input.grid(row=1, column=0, padx=(20, 0), pady=10,  sticky="nw")

        self.category_add_btn = customtkinter.CTkButton(self, text="Add", font=button_font, height=50,
                                                        width=50, command=self.on_add_button_clicked)
        self.category_add_btn.grid(row=1, column=1, padx=10, pady=10, sticky="n")

    def on_add_button_clicked(self):
        input_text = self.get_input()
        if input_text and self.command:
            self.command(input_text)

    def get_input(self):
        input_text = self.category_input.get().strip()
        print(f"Input text: {input_text}")
        if not input_text:
            messagebox.showerror("Input Error", "Input Field can't be empty")
        else:
            return input_text



