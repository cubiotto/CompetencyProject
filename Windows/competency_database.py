import customtkinter
import tkinter
from Styles.styles import title_font, h1_font, button_font



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
        text_var = tkinter.StringVar()

        self.category_input = customtkinter.CTkEntry(self.input_frame, width=100, height=50,
                                                     corner_radius=30, placeholder_text="Input Category",
                                                     placeholder_text_color="black")
        self.category_input.grid(row=0, column=0, padx=(40,0), pady=10, sticky="nw")