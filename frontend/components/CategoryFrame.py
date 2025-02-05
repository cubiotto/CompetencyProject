import customtkinter


class CategoryFrame(customtkinter.CTkFrame):
    def __init__(self, master, category_name):
        super().__init__(master)
        self.label = customtkinter.CTkLabel(self, text=category_name)
        self.label.grid(row=0, column=0, padx=10, pady=10)
