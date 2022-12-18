import sys
import customtkinter

from data.settings import Settings


class App(customtkinter.CTk):
    # CONSTRUCTOR
    def __init__(self):
        super().__init__()
        self.title = "AB Conseil app"
        self.resizable = False



    # METHODS
    def run(self) -> None:
        self.mainloop()



if __name__ == "__main__":
    sys.path.append("../data")

    app = App()
    app.run()
