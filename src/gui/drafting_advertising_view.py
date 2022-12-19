import os
import customtkinter



class DraftingAdvertisingView(customtkinter.CTkFrame):
    # CONSTRUCTOR
    def __init__(self, app: customtkinter.CTk):
        super().__init__(master=app)
        self.pack(padx=20, pady=20)

        self.__app = app

        self.__configure_grid()

        self.__build_label_and_text()
        self.__build_options()



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


    def __build_label_and_text(self) -> None:
        """
        SUMMARY
        -------
        This private method is used to create all labels and text widgets in the view.
        """
        excel_file_label = customtkinter.CTkLabel(master=self, text="Excel File :")
        excel_file_label.grid(row=0, column=0)

        self.__message_text_box = customtkinter.CTkTextbox(master=self, font=("Helvetica", 12))
        self.__message_text_box.grid(row=1, column=0, columnspan=3)
    

    def __build_options(self) -> None:
        """
        SUMMARY
        -------
        This private method is used to generate all option menu and combo box widgets in the view.
        """
        self.__excel_file_combo_box = customtkinter.CTkComboBox(master=self, values=[file for file in os.listdir(
            os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "..", "assets"))
            if (".xlsx" in file or ".xls" in file)])

        self.__excel_file_combo_box.grid(row=0, column=1, columnspan=2)
