import os
import customtkinter

from gui.generic_gui import *
from gui.pop_up_parameter import ParameterPopUp



class DraftingAdvertisingView(customtkinter.CTkFrame):
    # CONSTRUCTOR
    def __init__(self, app: customtkinter.CTk):
        """
        SUMMARY
        -------
        This constructor builds the frame and all widgets inside.

        ARGUMENTS
        ---------
            app : customtkinter.CTk
                The window of the application.
        """
        super().__init__(master=app)
        self.pack(padx=35, pady=35)

        self.__app = app
        self.__parameters_list = dict()

        self.__build_label_and_text()
        self.__build_options()
        self.__build_buttons()



    # GETTER
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
        self.__parameters_list[parameter_name] = letter_column, default_value
        self.__parameters_option_menu.configure(values=self.__parameters_list)


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

        self.__parameters_option_menu = customtkinter.CTkOptionMenu(master=self, values=self.__parameters_list)
        self.__parameters_option_menu.set("parameters list")
        self.__parameters_option_menu.grid(row=2, column=0, padx=(30, 6), pady=15)


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
        """
        SUMMARY
        -------
        This private method is the function linked with the 'remove parameter' button when it pressed.
        It delete the parameter selectioned in the option parameter menu.
        """
        if self.__parameters_list.pop(self.__parameters_option_menu.get(), None) is not None:
            self.__parameters_option_menu.set("parameters list")


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
        ParameterPopUp(self, True)
