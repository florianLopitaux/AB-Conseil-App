import customtkinter

from data.settings import Settings
from gui.home_view import HomeView
from gui.drafting_advertising_view import DraftingAdvertisingView
from gui.duplicate_analysis_view import DuplicateAnalysisView



class App(customtkinter.CTk):
    """
    SUMMARY
    -------
    This class is the window class that we instantiate to launch the application.

    METHODS
    -------
    - change_view(view_name: str) -> None 
    - run() -> None

        CONSTRUCTOR
        -----------
        - App()
    """
    # CONSTRUCTOR
    def __init__(self):
        """
        SUMMARY
        -------
        This constructor loads and genrates all things to start the application.
        """
        super().__init__()
        self.title("AB Conseil application")
        self.resizable(False, False)

        # create instance of Settings class and load data from the json configuration file
        Settings()

        # load home view
        self.__view = HomeView(self)



    # METHODS
    def change_view(self, view_name: str) -> None:
        """
        SUMMARY
        -------
        This method change the application view in terms of the view name that we passed as parameter.
        The name accepted are : 'HOME', 'DRAFT-ADVERTISE' and 'DUPLICATE-ANALYSIS'.

        ARGUMENTS
        ---------
            - view_name : str
                The name of the new view that we want set.
        """
        match view_name:
            case "HOME":
                self.__view = HomeView(self)
            case "DRAFT-ADVERTISE":
                self.__view = DraftingAdvertisingView(self)
            case "DUPLICATE-ANALYSIS":
                self.__view = DuplicateAnalysisView(self)


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
