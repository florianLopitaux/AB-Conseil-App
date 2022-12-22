import customtkinter

from data.settings import Settings
from gui.generic_gui import clear_frame
from gui.configuration_frame import ConfigurationView



class HomeView(customtkinter.CTkFrame):
    """
    SUMMARY
    -------
    This class manage the home view of the application.

    METHODS
    -------
    - build_buttons() -> None

        CONSTRUCTOR
        -----------
        - HomeView(app: App)
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
                The window of the application
        """
        super().__init__(master=app, fg_color="transparent")
        self.pack(ipadx=210, ipady=80)
        
        self.__app = app

        # title
        title_label = customtkinter.CTkLabel(master=self, text="AB Conseil Whatsapp app", font=("Comic Sans MS", 30, "bold"), wraplength=250)
        title_label.pack(pady=(50, 0))

        # buttons
        self.build_buttons()



    # METHODS
    def build_buttons(self) -> None:
        """
        SUMMARY
        -------
        This method is used to create and configurate all buttons on this view.
        """
        self.__container = customtkinter.CTkFrame(master=self)
        self.__container.pack(pady=(70, 0), ipadx=100, fill="none", expand=False)

        button_use_app = customtkinter.CTkButton(master=self.__container, command=self.__command_use_app,
                                                 text=Settings.get_instance().get_text("HomeView", "useAppButton"))
        button_use_app.pack(pady=(50, 10))

        button_duplicate_analysis = customtkinter.CTkButton(master=self.__container, command=self.__command_duplicate,
                                                            text=Settings.get_instance().get_text("HomeView", "duplicateAnalysisButton"))
        button_duplicate_analysis.pack(pady=(10, 30))

        button_settings = customtkinter.CTkButton(master=self.__container, command=self.__command_settings,
                                                  text=Settings.get_instance().get_text("HomeView", "settingsButton"))
        button_settings.pack(pady=10)

        button_exit = customtkinter.CTkButton(master=self.__container, command=self.__command_exit,
                                              text=Settings.get_instance().get_text("HomeView", "exitButton"))
        button_exit.pack(pady=(10, 50))



    # BUTTONS FUNCTION
    def __command_use_app(self) -> None:
        """
        SUMMARY
        -------
        This private method is the function linked with the 'use app' button when it pressed.
        It clear the currently view and change to the drafting advertising view.
        """
        clear_frame(self)
        self.__app.change_view('DRAFT-ADVERTISE')


    def __command_duplicate(self) -> None:
        pass


    def __command_settings(self) -> None:
        """
        SUMMARY
        -------
        This private method is the function linked with the 'settings' button when it pressed.
        It clears the currently content of the button frame and load the configuration view.
        """
        clear_frame(self.__container)
        self.__container = ConfigurationView(self)


    def __command_exit(self) -> None:
        """
        SUMMARY
        -------
        This private method is the function linked with the 'exit' button when it pressed.
        It closes the window and quits the application.
        """
        self.__app.destroy()
