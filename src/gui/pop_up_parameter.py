import customtkinter



class ParameterPopUp(customtkinter.CTkToplevel):
    # CONSTRUCTOR
    def __init__(self, parent: customtkinter.CTkFrame, isKeyParameter: bool):
        super().__init__()
        self.title("Add new parameter")
        self.__parent = parent

        self.__build_labels()
        self.__build_entries()

        buttonRegister = customtkinter.CTkButton(master=self, command=self.__command_register, text="Register")
        buttonRegister.grid(row=3, column=0, columnspan=2, pady=(30, 20))



    # METHODS
    def __build_labels(self) -> None:
        name_label = customtkinter.CTkLabel(master=self, text="Name :")
        name_label.grid(row=0, column=0, padx=(40, 10), pady=(30, 10))

        default_value_label = customtkinter.CTkLabel(master=self, text="Default Value :")
        default_value_label.grid(row=1, column=0, padx=(40, 10), pady=15)

        letter_column_label = customtkinter.CTkLabel(master=self, text="Column Letter :")
        letter_column_label.grid(row=2, column=0, padx=(40, 10), pady=10)

    
    def __build_entries(self) -> None:
        self.__name_entry = customtkinter.CTkEntry(master=self)
        self.__name_entry.grid(row=0, column=1, sticky="ew", padx=(10, 40), pady=(30, 10))

        self.__default_value_entry = customtkinter.CTkEntry(master=self)
        self.__default_value_entry.grid(row=1, column=1, sticky="ew", padx=(10, 40), pady=15)

        self.__letter_column_entry = customtkinter.CTkEntry(master=self)
        self.__letter_column_entry.grid(row=2, column=1, sticky="ew", padx=(10, 40), pady=10)



    # BUTTON FUNCTION
    def __command_register(self) -> None:
        self.__parent.addParameter(self.__name_entry.get(), self.__default_value_entry.get(), self.__letter_column_entry.get())
        self.destroy()
