import os
import customtkinter

from gui.generic_gui import create_red_button, create_green_button



class DraftingAdvertisingView(customtkinter.CTkFrame):
    # CONSTRUCTOR
    def __init__(self, app: customtkinter.CTk):
        super().__init__(master=app)
        self.pack(padx=35, pady=35)

        self.__app = app

        self.__build_label_and_text()
        self.__build_options()
        self.__build_buttons()



    # METHODS
    def __build_label_and_text(self) -> None:
        """
        SUMMARY
        -------
        This private method is used to create all labels and text widgets in the view.
        """
        excel_file_label = customtkinter.CTkLabel(master=self, text="Excel File :")
        excel_file_label.grid(row=0, column=0, pady=(30, 15))

        self.__message_text_box = customtkinter.CTkTextbox(master=self, font=("Helvetica", 12))
        self.__message_text_box.grid(row=1, column=0, columnspan=3, sticky="nesw", padx=30, pady=15)
    

    def __build_options(self) -> None:
        """
        SUMMARY
        -------
        This private method is used to generate all option menu and combo box widgets in the view.
        """
        self.__excel_file_combo_box = customtkinter.CTkComboBox(master=self, values=[file for file in os.listdir(
            os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "..", "assets"))
            if (".xlsx" in file or ".xls" in file)])

        self.__excel_file_combo_box.set("")
        self.__excel_file_combo_box.grid(row=0, column=1, columnspan=2, sticky="ew", padx=(0, 30), pady=(30, 15))

        self.__parameters_list = customtkinter.CTkOptionMenu(master=self, values=[])
        self.__parameters_list.set("parameters list")
        self.__parameters_list.grid(row=2, column=0, padx=(30, 6), pady=15)


    def __build_buttons(self) -> None:
        """
        SUMMARY
        -------
        This private method is used to create all buttons widgets in the view.
        """
        remove_parameter_button = customtkinter.CTkButton(master=self, command=self.__command_delete, text="Remove parameter")
        remove_parameter_button.grid(row=2, column=1, padx=6, pady=15)

        add_parameter_button = customtkinter.CTkButton(master=self, command=self.__command_append, text="Add parameter")
        add_parameter_button.grid(row=2, column=2, padx=(6, 30), pady=15)

        back_button = create_red_button(self, "Back to Menu")
        back_button.configure(command=self.__command_back)
        back_button.grid(row=3, column=0, columnspan=2, pady=(30, 15))

        validate_button = create_green_button(self, "Validate")
        validate_button.configure(command=self.__command_validate)
        validate_button.grid(row=3, column=1, columnspan=2, pady=(30, 15))



    # BUTTONS FUNCTION
    def __command_delete(self) -> None:
        pass


    def __command_append(self) -> None:
        pass


    def __command_back(self) -> None:
        pass

    
    def __command_validate(self) -> None:
        pass
