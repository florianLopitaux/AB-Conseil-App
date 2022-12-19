import customtkinter

from data.settings import Settings



class ConfigurationView(customtkinter.CTkFrame):
    # CONSTRUCTOR
    def __init__(self, app: customtkinter.CTk):
        super().__init__(master=app)
        self.pack(pady=(70, 0), ipadx=100)
        self.__app = app

        self.__configure_grid()

        self.__build_options_menu()



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
        self.__option_colors_theme.set(Settings.get_instance().get_colors_theme())
        self.__option_colors_theme.grid(row=1, column=0, columnspan=2, pady=15)
