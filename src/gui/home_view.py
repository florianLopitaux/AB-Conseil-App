import customtkinter



class HomeView(customtkinter.CTkFrame):
    # CONSTRUCTOR
    def __init__(self, app: customtkinter.CTk):
        """
        SUMMARY
        -------
        This constructor

        ARGUMENTS
        ---------
            app : customtkinter.CTk
                The window of the application
        """
        super().__init__(master=app, fg_color="transparent")
        self.pack(ipadx=200, ipady=70)

        # title
        title_label = customtkinter.CTkLabel(master=self, text="AB Conseil Whatsapp app", wraplength=300,
                                             font=("Helvetica bold", 16))
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

        button_use_app = customtkinter.CTkButton(master=self.__container, text="Use app")
        button_use_app.pack(pady=(50, 30))

        button_settings = customtkinter.CTkButton(master=self.__container, text="Settings")
        button_settings.pack(pady=10)

        button_exit = customtkinter.CTkButton(master=self.__container, text="Exit")
        button_exit.pack(pady=(10, 50))
