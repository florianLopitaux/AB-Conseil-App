import customtkinter

from data.settings import Settings
from gui.home_view import HomeView



class App(customtkinter.CTk):
    # CONSTRUCTOR
    def __init__(self):
        super().__init__()
        self.title("AB Conseil application")
        self.resizable(False, False)

        # create instance of Settings class and load data from the json configuration file
        Settings()

        # load home view
        self.__view = HomeView(self)



    # SETTER
    def changeView(self, view: customtkinter.CTkFrame) -> None:
        """
        SUMMARY
        -------
        This method is the setter to the 'view' attribute.

        ARGUMENTS:
            view : customtkinter.CTkFrame
                The new view that we want set.
        """
        self.__view = view



    # METHODS
    def run(self) -> None:
        """
        SUMMARY
        -------
        This method launches the application.
        """
        self.mainloop()



if __name__ == "__main__":
    app = App()
    app.run()
