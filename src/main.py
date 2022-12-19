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



    # METHODS
    def run(self) -> None:
        self.mainloop()
    

    def changeView(self, view: customtkinter.CTkFrame) -> None:
        self.__view = view



if __name__ == "__main__":
    app = App()
    app.run()
