import customtkinter



class HomeFrame(customtkinter.CTkFrame):
    # CONSTRUCTOR
    def __init__(self, app: customtkinter.CTk):
        super.__init__(master=app)

        self.pack()
