import customtkinter
from frontend.styles.fonts import h1_font, button_font
from customtkinter import CTkLabel


class InputField(customtkinter.CTkFrame):
    def __init__(self, master, input_field_name, placeholder_name):
        super().__init__(master, fg_color="transparent")
        self.input_field_name = input_field_name
        self.placeholder_name = placeholder_name
        self.category_label = CTkLabel(self, text=input_field_name, font=h1_font, padx=5, pady=5)
        self.category_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.category_input = customtkinter.CTkEntry(self, width=220, height=50)
        self.category_input.grid(row=1, column=0, padx=(40, 0), pady=10,  sticky="nw")

        self.category_add_btn = customtkinter.CTkButton(self, text="Add", font=button_font, height=50,
                                                        width=50, command=self.get_input())
        self.category_add_btn.grid(row=1, column=1, padx=10, sticky="n")

    def get_input(self):
        input_text = self.category_input.get()
        print(f"Input text: {input_text}")

