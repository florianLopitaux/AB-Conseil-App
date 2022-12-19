import customtkinter

from main import App



class DraftingAdvertisingView(customtkinter.CTkFrame):
    # CONSTRUCTOR
    def __init__(self, app: App):
        super().__init__(master=app)
        self.pack(padx=20, pady=20)

        self.__app = app

        self.__configure_grid()



    # METHODS
    def __configure_grid(self) -> None:
        """
        SUMMARY
        -------
        This private method is called only in the constructor.
        It configures the rows and columns of the grid frame.
        """
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
            
            if i == 1:
                self.grid_rowconfigure(i, weight=2)
            else:
                self.grid_rowconfigure(i, weight=1)
        
        self.grid_rowconfigure(3, weight=1)
