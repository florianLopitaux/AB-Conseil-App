import customtkinter



class ParameterPopUp(customtkinter.CTkToplevel):
    # CONSTRUCTOR
    def __init__(self, parent: customtkinter.CTkFrame, isKeyParameter: bool):
        """
        SUMMARY
        -------
        This constructor builds the pop-up and all widgets inside.

        ARGUMENTS
        ---------
            - parent : customtkinter.CTkFrame
                The parent frame where the pop-up has been called. (DraftingAdvertisingView to add parameter)
            - isKeyParameter : bool
                The boolean to know if the pop-up is for the main parameter (phone number) or a generic parameter.
        """
        super().__init__()
        self.title("Add new parameter")
        self.__parent = parent
        self.__isKeyParameter = isKeyParameter

        self.__build_labels()
        self.__build_entries()

        buttonRegister = customtkinter.CTkButton(master=self, command=self.__command_register, text="Register")
        if self.__isKeyParameter:
            buttonRegister.grid(row=5, column=0, columnspan=2, pady=(30, 20))
        else:
            buttonRegister.grid(row=3, column=0, columnspan=2, pady=(30, 20))



    # METHODS
    def __build_labels(self) -> None:
        """
        SUMMARY
        -------
        This private method is called only in the constructor and is used to create all labels descriptor to entries.
        """
        name_label = customtkinter.CTkLabel(master=self, text="Name :")
        name_label.grid(row=0, column=0, padx=(40, 10), pady=(30, 10))

        default_value_label = customtkinter.CTkLabel(master=self, text="Default Value :")
        default_value_label.grid(row=1, column=0, padx=(40, 10), pady=15)

        letter_column_label = customtkinter.CTkLabel(master=self, text="Column Letter :")
        letter_column_label.grid(row=2, column=0, padx=(40, 10), pady=10)

        if self.__isKeyParameter:
            start_row_label = customtkinter.CTkLabel(master=self, text="Start Row :")
            start_row_label.grid(row=3, column=0, padx=(40, 10), pady=15)

            end_row_label = customtkinter.CTkLabel(master=self, text="End Row :")
            end_row_label.grid(row=4, column=0, padx=(40, 10), pady=10)

    
    def __build_entries(self) -> None:
        """
        SUMMARY
        -------
        This private method is called only in the constructor and is used to create all entries to get the user input data.
        """
        self.__name_entry = customtkinter.CTkEntry(master=self)
        self.__name_entry.grid(row=0, column=1, sticky="ew", padx=(10, 40), pady=(30, 10))

        self.__default_value_entry = customtkinter.CTkEntry(master=self)
        self.__default_value_entry.grid(row=1, column=1, sticky="ew", padx=(10, 40), pady=15)

        self.__letter_column_entry = customtkinter.CTkEntry(master=self)
        self.__letter_column_entry.grid(row=2, column=1, sticky="ew", padx=(10, 40), pady=10)

        if self.__isKeyParameter:
            self.__start_row_entry = customtkinter.CTkEntry(master=self)
            self.__start_row_entry.grid(row=3, column=1, sticky="ew", padx=(10, 40), pady=15)

            self.__end_row_entry = customtkinter.CTkEntry(master=self)
            self.__end_row_entry.grid(row=4, column=1, sticky="ew", padx=(10, 40), pady=10)



    # BUTTON FUNCTION
    def __command_register(self) -> None:
        """
        SUMMARY
        -------
        This private method is the function linked with the 'register' button when it pressed.
        It adds the new parameter to the drafting advertising view and closes itself.
        """
        self.__parent.add_parameter(self.__name_entry.get(), self.__default_value_entry.get(), self.__letter_column_entry.get())
        self.destroy()
