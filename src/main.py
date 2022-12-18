import customtkinter


class App(customtkinter.CTk):
    # CONSTRUCTOR
    def __init__(self):
        super().__init__()



    # METHODS
    def run(self) -> None:
        self.mainloop()



if __name__ == "__main__":
    app = App()
    app.run()
