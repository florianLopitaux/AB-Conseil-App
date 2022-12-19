import customtkinter



class ParameterPopUp(customtkinter.CTkToplevel):
    # CONSTRUCTOR
    def __init__(self, parent: customtkinter.CTkFrame, isKeyParameter: bool):
        super().__init__()
        self.__parent = parent

        self.__build_labels()
        self.__build_entries()

        buttonRegister = customtkinter.CTkButton(master=self, command=self.__command_register, text="Register")
        buttonRegister.grid(row=3, column=0, columnspan=2, pady=(30, 20))



    # METHODS
    def __build_labels(self) -> None:
        pass

    
    def __build_entries(self) -> None:
        pass



    # BUTTON FUNCTION
    def __command_register(self) -> None:
        pass
