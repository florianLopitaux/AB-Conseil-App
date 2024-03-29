import os
from tkinter import messagebox
import customtkinter

from data.settings import Settings
from data.excel_utils import check_file
from data.whatsapp_manager import get_all_messages_parameters
from gui.generic_gui import *
from gui.pop_up_parameter import ParameterPopUp



class DraftingAdvertisingView(customtkinter.CTkFrame):
    """
    SUMMARY
    -------
    This class is the frame that manage all user interface to prepare the messages wave on whatsapp.

    METHODS
    -------
        CONSTRUCTOR
        -----------
        - DraftingAdvertisingView(app: customtkinter.CTk)

        GETTERS
        -------
        - get_parameters() -> dict[str, tuple[str, str]]
        - get_message() -> str
        - get_excel_file() -> str

        SETTER
        ------
        - add_parameter(parameter_name: str, default_value: str, letter_column: str) -> None
    """
    # CONSTRUCTOR
    def __init__(self, app: customtkinter.CTk):
        """
        SUMMARY
        -------
        This constructor builds the frame and all widgets inside.

        ARGUMENTS
        ---------
            - app : customtkinter.CTk
                The window of the application.
        """
        super().__init__(master=app)
        self.pack(padx=35, pady=35)

        self.__app = app
        self.__parameters_list = dict()

        self.__build_label_and_text()
        self.__build_options()
        self.__build_buttons()



    # GETTERS
    def get_parameters(self) -> dict[str, tuple[str, str]]:
        """
        SUMMARY
        -------
        This method is the getter of the 'parameters_list' attribute.
        The attribute stores all parameters register by the user.

        RETURNS
        -------
        dict[str, tuple[str, str]]: The dictionary that contains all parameters.
                                    Format: key => parameter_name
                                            value => default_value, letter_column
        """
        return self.__parameters_list


    def get_message(self) -> str:
        """
        SUMMARY
        -------
        This method is the getter of the text in the message text box.

        RETURNS
        -------
        str: The message writes by the user.
        """
        return self.__message_text_box.get("1.0", customtkinter.END)


    def get_excel_file(self) -> str:
        """
        SUMMARY
        -------
        This method is the getter of the excel file which contains all data.

        RETRUNS
        -------
        str: The name of the excel file.
        """
        return self.__excel_file_combo_box.get()    



    # SETTER
    def add_parameter(self, parameter_name: str, default_value: str, letter_column: str) -> None:
        """
        SUMMARY
        -------
        This method is the setter of the 'parameters_list' attribute.
        It append the new parameter to the attribute and update the parameters option menu.

        ARGUMENTS
        ---------
            - parameter_name : str
                The name of the parameter which must correspond with those written in the text.
            - default_value : str
                The default value of the parameter if the data is missing in the excel file.
            - letter_column : str
                The letter column of the parameter corresponding in the excel file.
        """
        self.__parameters_list[parameter_name] = default_value, letter_column
        self.__parameters_option_menu.configure(values=self.__parameters_list)


    # METHODS
    def __build_label_and_text(self) -> None:
        """
        SUMMARY
        -------
        This private method is used to create all labels and text widgets in the view.
        """
        excel_file_label = customtkinter.CTkLabel(master=self, text=Settings.get_instance().get_text("DraftingAdvertisingView", "fileLabel"))
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
            if ".xls" in file])

        self.__excel_file_combo_box.set("")
        self.__excel_file_combo_box.grid(row=0, column=1, columnspan=2, sticky="ew", padx=(0, 30), pady=(30, 15))

        self.__parameters_option_menu = customtkinter.CTkOptionMenu(master=self, values=self.__parameters_list)
        self.__parameters_option_menu.set(Settings.get_instance().get_text("DraftingAdvertisingView", "parameterTextOptionMenu"))
        self.__parameters_option_menu.grid(row=2, column=0, padx=(30, 6), pady=15)


    def __build_buttons(self) -> None:
        """
        SUMMARY
        -------
        This private method is used to create all buttons widgets in the view.
        """
        remove_parameter_button = customtkinter.CTkButton(master=self, command=self.__command_delete,
                                                          text=Settings.get_instance().get_text("DraftingAdvertisingView", "removeParameterButton"))
        remove_parameter_button.grid(row=2, column=1, padx=6, pady=15)

        add_parameter_button = customtkinter.CTkButton(master=self, command=self.__command_append,
                                                       text=Settings.get_instance().get_text("DraftingAdvertisingView", "addParameterButton"))
        add_parameter_button.grid(row=2, column=2, padx=(6, 30), pady=15)

        back_button = create_red_button(self, Settings.get_instance().get_text("DraftingAdvertisingView", "backButton"))
        back_button.configure(command=self.__command_back)
        back_button.grid(row=3, column=0, columnspan=2, pady=(30, 15))

        validate_button = create_green_button(self, Settings.get_instance().get_text("DraftingAdvertisingView", "validateButton"))
        validate_button.configure(command=self.__command_validate)
        validate_button.grid(row=3, column=1, columnspan=2, pady=(30, 15))



    # BUTTONS FUNCTION
    def __command_delete(self) -> None:
        """
        SUMMARY
        -------
        This private method is the function linked with the 'remove parameter' button when it pressed.
        It delete the parameter selectioned in the option parameter menu.
        """
        if self.__parameters_list.pop(self.__parameters_option_menu.get(), None) is not None:
            self.__parameters_option_menu.set(Settings.get_instance().get_text("DraftingAdvertisingView", "parameterTextOptionMenu"))


    def __command_append(self) -> None:
        """
        SUMMARY
        -------
        This private method is the function linked with the 'add parameter' button when it pressed.
        It generate a pop-up to add a new parameter to the message.
        """
        ParameterPopUp(self, False)


    def __command_back(self) -> None:
        """
        SUMMARY
        -------
        This private method is the function linked with the 'back to menu' button when it pressed.
        It destroy this current view and rebuild a new home view.
        """
        clear_frame(self)
        self.__app.change_view('HOME')

    
    def __command_validate(self) -> None:
        """
        This private method is the function linked with the 'validate' button when it pressed.
        It launch the pop-up parameter to phone number (special data to inform) before starting the send messages wave.
        """
        if not check_file(self.get_excel_file()):
            messagebox.showerror("AB Conseil application error !", Settings.get_instance().get_text("MessageBoxError", "excelFileExists").format(self.get_excel_file()))
            return None

        if ".xls" not in self.get_excel_file():
            messagebox.showerror("AB Conseil application error !", Settings.get_instance().get_text("MessageBoxError", "fileNotAnExcelFile").format(self.get_excel_file()))
            return None
        
        parameters = get_all_messages_parameters(self.get_message())

        if parameters is None:
            messagebox.showerror("AB Conseil application error !", Settings.get_instance().get_text("MessageBoxError", "nbBracketsError"))
            return None
        
        for param_name in parameters:
            if param_name not in self.__parameters_list.keys():
                messagebox.showerror("AB Conseil application error !", Settings.get_instance().get_text("MessageBoxError", "notRegisterAllParameters"))
                return None

        ParameterPopUp(self, True)
