import customtkinter

from data.settings import Settings



class DuplicateAnalysisView(customtkinter.CTkFrame):
    # CONSTRUCTOR
    def __init__(self, app: customtkinter.CTk) -> None:
        super().__init__(master=app)
        self.pack(padx=35, pady=35)

        self.__app = app

        self.__build_labels()
        self.__build_entries()



    # METHODS
    def __build_labels(self) -> None:
        """
        SUMMARY
        -------
        This private method is called only in the constructor and is used to create all labels of the view.
        """
        excel_file_label = customtkinter.CTkLabel(master=self, text=Settings.get_instance().get_text("DraftingAdvertisingView", "fileLabel"))
        excel_file_label.grid(row=0, column=0, pady=30)

        letter_column_label = customtkinter.CTkLabel(master=self, text=Settings.get_instance().get_text("PopUpParameter", "letterColumnLabel"))
        letter_column_label.grid(row=1, column=0, columnspan=2, pady=10)

        start_row_label = customtkinter.CTkLabel(master=self, text=Settings.get_instance().get_text("PopUpParameter", "firstRowLabel"))
        start_row_label.grid(row=2, column=0, columnspan=2, pady=10)

        end_row_label = customtkinter.CTkLabel(master=self, text=Settings.get_instance().get_text("PopUpParameter", "lastRowLabel"))
        end_row_label.grid(row=3, column=0, columnspan=2, pady=10)
    

    def __build_entries(self) -> None:
        """
        SUMMARY
        -------
        This private method is called only in the constructor and is used to create all entries to get the user input data.
        """
        self.__letter_column_entry = customtkinter.CTkEntry(master=self)
        self.__letter_column_entry.grid(row=1, column=1, columnspan=2, sticky="ew", pady=10)

        self.__start_row_entry = customtkinter.CTkEntry(master=self)
        self.__start_row_entry.grid(row=2, column=1, columnspan=2, sticky="ew", pady=10)

        self.__end_row_entry = customtkinter.CTkEntry(master=self)
        self.__end_row_entry.grid(row=3, column=1, columnspan=2, sticky="ew", pady=10)
