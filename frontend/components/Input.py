import customtkinter
from frontend.styles.fonts import h1_font, button_font
from customtkinter import CTkLabel

class SettingsInputSection(customtkinter.CTkFrame):
    def __init__(self, master, input_field_name):
        super().__init__(master, fg_color="transparent")
        self.input_field_name = input_field_name
        self.category_label = CTkLabel(self, text=input_field_name, font=h1_font, padx=5, pady=5)
        self.category_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.category_input = customtkinter.CTkEntry(self, width=220, height=50)
        self.category_input.grid(row=1, column=0, padx=(10, 0), sticky="nw")

        self.category_add_btn = customtkinter.CTkButton(self, text="Add", font=button_font, height=50,
                                                        width=50, command=self.add_category)
        self.category_add_btn.grid(row=1, column=1, padx=10, sticky="n")

        self.category_list_frame = customtkinter.CTkScrollableFrame(self, height=300, width=200)
        self.category_list_frame.grid(row=2, column=0, padx=10, pady=10)

        self.category_list = []

    def add_category(self):
        category_data = self.category_input.get()
        self.category_list.append(category_data)
        self.category_input.delete(0, "end")  # Clear the input field

        for i, category in enumerate(self.category_list, start=1):
            category_label = CTkLabel(self.category_list_frame, text=f"{i}. {category}")
            category_label.grid(row=i, column=0, padx=10, pady=10, sticky="nw")


