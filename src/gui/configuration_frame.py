import customtkinter

from data.settings import Settings
from gui.generic_gui import *



class ConfigurationView(customtkinter.CTkFrame):
    """
    SUMMARY
    -------
    This class is the frame that manage all user interface with application settings.
    It called in the home view with the 'settings' button.
    If the user pressed the 'cancel' button all changes will not be taken into account.
    Conversely, if he presses the 'apply' button.

    METHODS
    -------
        CONSTRUCTOR
        -----------
        - ConfigurationView(container: customtkinter.CTkFrame)
    """
    # CONSTRUCTOR
    def __init__(self, container: customtkinter.CTkFrame):
        """
        SUMMARY
        -------
        This constructor builds the frame and all widgets inside.

        ARGUMENTS
        ---------
            - container : customtkinter.CTkFrame
                The frame (master) that contains the configuration view.
        """
        super().__init__(master=container)
        self.pack(pady=(70, 0), ipadx=100)

        self.__container = container

        self.__configure_grid()

        self.__build_options_menu()
        self.__build_radio_buttons_section()
        self.__build_buttons()



    # METHODS
    def __configure_grid(self) -> None:
        """
        SUMMARY
        -------
        This private method is called only in the constructor.
        It configures the rows and columns of the grid frame.
        """
        for i in range(5):
            self.rowconfigure(i, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


    def __build_options_menu(self) -> None:
        """
        SUMMARY
        -------
        This private method is called only in the constructor.
        It generates the two options menu widgets of the frame (appearance mode and color theme)
        """
        self.__option_appearance_mode = customtkinter.CTkOptionMenu(master=self, values=["System", "Dark", "Light"])
        self.__option_appearance_mode.set(Settings.get_instance().get_appearance_mode())
        self.__option_appearance_mode.grid(row=0, column=0, columnspan=2, pady=(30, 15))

        self.__option_color_theme = customtkinter.CTkOptionMenu(master=self, values=["blue", "green"])
        self.__option_color_theme.set(Settings.get_instance().get_color_theme())
        self.__option_color_theme.grid(row=1, column=0, columnspan=2, pady=15)


    def __build_radio_buttons_section(self) -> None:
        """
        SUMMARY
        -------
        This private method is called only in the constructor.
        It generates the two radio buttons widgets and corresponding section label of the frame.
        """
        desc_radio_buttons = customtkinter.CTkLabel(master=self, text=Settings.get_instance().get_text("SettingsView", "phoneFormatLabel"))
        desc_radio_buttons.grid(row=2, column=0, columnspan=2, pady=(15, 5))

        self.__radio_button_var = customtkinter.IntVar()
        if (Settings.get_instance().get_phone_format() == "06"):
            self.__radio_button_var.set(0)
        else:
            self.__radio_button_var.set(1)

        radioButton06 = customtkinter.CTkRadioButton(master=self, text="06...", variable=self.__radio_button_var, value=0)
        radioButton06.grid(row=3, column=0, pady=(5, 15))

        radioButton33 = customtkinter.CTkRadioButton(master=self, text="+33...", variable=self.__radio_button_var, value=1)
        radioButton33.grid(row=3, column=1, pady=(5, 15))


    def __build_buttons(self) -> None:
        """
        SUMMARY
        -------
        This private method is called only in the constructor.
        It generates the two buttons widgets of the frame.
        """
        cancel_button = create_red_button(self, Settings.get_instance().get_text("SettingsView", "cancelButton"))
        cancel_button.configure(command=self.__command_cancel)
        cancel_button.grid(row=4, column=0, pady=(30, 8))

        validate_button = create_green_button(self, Settings.get_instance().get_text("SettingsView", "applyButton"))
        validate_button.configure(command=self.__command_validate)
        validate_button.grid(row=4, column=1, pady=(30, 8))



    # BUTTONS FUNCTION
    def __command_cancel(self) -> None:
        """
        SUMMARY
        -------
        This private method is the function linked with the 'cancel' button when it pressed.
        It destroy this view and rebuild the home view without save changes.
        """
        clear_frame(self)
        self.__container.build_buttons()


    def __command_validate(self) -> None:
        """
        SUMMARY
        -------
        This private method is the function linked with the 'validate' button when it pressed.
        It saves changes and rebuild the home view.
        """
        Settings.get_instance().set_appearance_mode(self.__option_appearance_mode.get())
        Settings.get_instance().set_color_theme(self.__option_color_theme.get())

        if (self.__radio_button_var.get() == 0):
            Settings.get_instance().set_phone_format("06")
        else:
            Settings.get_instance().set_phone_format("+33")
        
        clear_frame(self)
        self.__container.build_buttons()
