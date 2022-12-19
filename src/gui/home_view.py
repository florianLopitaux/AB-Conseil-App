import customtkinter

from generic_gui import clear_widgets
from configuration_view import ConfigurationView



class HomeView(customtkinter.CTkFrame):
    # CONSTRUCTOR
    def __init__(self, app: customtkinter.CTk):
        """
        SUMMARY
        -------
        This constructor builds the frame and all widgets inside.

        ARGUMENTS
        ---------
            app : customtkinter.CTk
                The window of the application
        """
        super().__init__(master=app, fg_color="transparent")
        self.pack(ipadx=210, ipady=80)
        self.__app = app

        # title
        title_label = customtkinter.CTkLabel(master=self, text="AB Conseil Whatsapp app", font=("Comic Sans MS", 30, "bold"), wraplength=250)
        title_label.pack(pady=(50, 0))

        # buttons
        self.__buildButtons(app)



    # METHODS
    def __buildButtons(self, app: customtkinter.CTk) -> None:
        """
        SUMMARY
        -------
        This private method is used in the constructor to create and configurate all buttons on this frame.

        ARGUMENTS
        ---------
            app : customtkinter.CTk
                The window of the application
        """
        self.__container = customtkinter.CTkFrame(master=self)
        self.__container.pack(pady=(70, 0), ipadx=100, fill="none", expand=False)

        button_use_app = customtkinter.CTkButton(master=self.__container, command=self.__command_use_app, text="Use app")
        button_use_app.pack(pady=(50, 30))

        button_settings = customtkinter.CTkButton(master=self.__container, command=self.__command_settings, text="Settings")
        button_settings.pack(pady=10)

        button_exit = customtkinter.CTkButton(master=self.__container, command=self.__command_exit, text="Exit")
        button_exit.pack(pady=(10, 50))


    def __command_use_app(self) -> None:
        pass


    def __command_settings(self) -> None:
        """
        SUMMARY
        -------
        This method is the function linked with the 'settings' button when it pressed.
        It clears the currently content of the button frame and load the configuration view.
        """
        clear_widgets(self.__container)
        self.__container = ConfigurationView(self.__app)


    def __command_exit(self) -> None:
        """
        SUMMARY
        -------
        This method is the function linked with the 'exit' button when it pressed.
        It closes the window and quits the application.
        """
        self.__app.destroy()
