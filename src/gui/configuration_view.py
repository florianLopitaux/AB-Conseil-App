import customtkinter

from data.settings import Settings
from gui.generic_gui import *



class ConfigurationView(customtkinter.CTkFrame):
    # CONSTRUCTOR
    def __init__(self, container: customtkinter.CTkFrame):
        super().__init__(master=container)
        self.pack(pady=(70, 0), ipadx=100)

        self.__container = container
        self.__current_appearance_mode = Settings.get_instance().get_appearance_mode()
        self.__current_color_theme = Settings.get_instance().get_color_theme()

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
        self.__options_appearance_mode = customtkinter.CTkOptionMenu(master=self, values=["System", "Dark", "Light"])
        self.__options_appearance_mode.set(Settings.get_instance().get_appearance_mode())
        self.__options_appearance_mode.grid(row=0, column=0, columnspan=2, pady=(30, 15))

        self.__option_colors_theme = customtkinter.CTkOptionMenu(master=self, values=["blue", "green"])
        self.__option_colors_theme.set(Settings.get_instance().get_color_theme())
        self.__option_colors_theme.grid(row=1, column=0, columnspan=2, pady=15)


    def __build_radio_buttons_section(self) -> None:
        """
        SUMMARY
        -------
        This private method is called only in the constructor.
        It generates the two radio buttons widgets and corresponding section label of the frame.
        """
        desc_radio_buttons = customtkinter.CTkLabel(master=self, text="Phone number format")
        desc_radio_buttons.grid(row=2, column=0, columnspan=2, pady=(15, 5))

        radioButton06 = customtkinter.CTkRadioButton(master=self, text="06...", value=0)
        radioButton06.grid(row=3, column=0, pady=(5, 15))

        radioButton33 = customtkinter.CTkRadioButton(master=self, text="+33...", value=1)
        radioButton33.grid(row=3, column=1, pady=(5, 15))


    def __build_buttons(self) -> None:
        """
        SUMMARY
        -------
        This private method is called only in the constructor.
        It generates the two buttons widgets of the frame.
        """
        cancel_button = create_red_button(self, "Cancel")
        cancel_button.configure(command=self.__command_cancel)
        cancel_button.grid(row=4, column=0, pady=(30, 8))

        validate_button = create_green_button(self, "Apply")
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
        pass
