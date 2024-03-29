import customtkinter

from data.settings import Settings
from data.whatsapp_manager import launch_messages_wave



class ParameterPopUp(customtkinter.CTkToplevel):
    """
    SUMMARY
    -------
    This class is the frame that manage the user interface to configure a new parameter.

    METHODS
    -------
        CONSTRUCTOR
        -----------
        - ParameterPopUp(parent: customtkinter.CTkFrame, isKeyParameter: bool)
    """
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

        if isKeyParameter:
            self.title("Phone number parameter")
        else:
            self.title("Add new parameter")

        self.__parent = parent
        self.__isKeyParameter = isKeyParameter

        self.__build_labels()
        self.__build_entries()

        buttonRegister = customtkinter.CTkButton(master=self, command=self.__command_register,
                                                 text=Settings.get_instance().get_text("PopUpParameter", "registerButton"))
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
        if not self.__isKeyParameter:
            name_label = customtkinter.CTkLabel(master=self, text=Settings.get_instance().get_text("PopUpParameter", "parameterNameLabel"))
            name_label.grid(row=0, column=0, padx=(40, 10), pady=(30, 10))

            default_value_label = customtkinter.CTkLabel(master=self, text=Settings.get_instance().get_text("PopUpParameter", "defaultValueLabel"))
            default_value_label.grid(row=1, column=0, padx=(40, 10), pady=15)

        letter_column_label = customtkinter.CTkLabel(master=self, text=Settings.get_instance().get_text("PopUpParameter", "letterColumnLabel"))
        letter_column_label.grid(row=2, column=0, padx=(40, 10), pady=10)

        if self.__isKeyParameter:
            start_row_label = customtkinter.CTkLabel(master=self, text=Settings.get_instance().get_text("PopUpParameter", "firstRowLabel"))
            start_row_label.grid(row=3, column=0, padx=(40, 10), pady=15)

            end_row_label = customtkinter.CTkLabel(master=self, text=Settings.get_instance().get_text("PopUpParameter", "lastRowLabel"))
            end_row_label.grid(row=4, column=0, padx=(40, 10), pady=10)

    
    def __build_entries(self) -> None:
        """
        SUMMARY
        -------
        This private method is called only in the constructor and is used to create all entries to get the user input data.
        """
        if not self.__isKeyParameter:
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
        if self.__isKeyParameter:
            # store input data before destroy the pop-up because impossible to get after
            letter_column = self.__letter_column_entry.get()
            start_row = int(self.__start_row_entry.get())
            end_row = int(self.__end_row_entry.get())

            self.destroy()

            launch_messages_wave(self.__parent, (letter_column.upper(), start_row, end_row))
        
        else:
            self.__parent.add_parameter(self.__name_entry.get(), self.__default_value_entry.get(), self.__letter_column_entry.get().upper())
            self.destroy()
