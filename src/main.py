import customtkinter

from data.settings import Settings
from gui.home_frame import HomeFrame



class App(customtkinter.CTk):
    # CONSTRUCTOR
    def __init__(self):
        super().__init__()
        self.title = "AB Conseil app"
        self.resizable = False

        # create instance of Settings class and load data from the json configuration file
        Settings()

        self.__container = HomeFrame(self)



    # METHODS
    def run(self) -> None:
        self.mainloop()



if __name__ == "__main__":
    app = App()
    app.run()
