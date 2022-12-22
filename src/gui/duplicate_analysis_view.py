import os
from tkinter import messagebox
import customtkinter

from data.settings import Settings
from data.excel_utils import check_file, check_duplicates
from gui.generic_gui import clear_frame, create_red_button



class DuplicateAnalysisView(customtkinter.CTkFrame):
    """
    SUMMARY
    -------
    This class is the frame that manage all user interface to analysis duplicates in an excel file.

    METHODS
    -------
        CONSTRUCTOR
        -----------
        - DuplicateAnalysisView(app: customtkinter.CTk)
    """
    # CONSTRUCTOR
    def __init__(self, app: customtkinter.CTk):
        """
        SUMMARY
        -------
        This constructor builds the frame and all widgets of the view.

        ARGUMENTS
        ---------
            - app : customtkinter.CTk
                The window of the application.
        """
        super().__init__(master=app)

        self.__app = app

        self.__back_button = create_red_button(self.__app, Settings.get_instance().get_text("DuplicateAnalysisView", "backButton"))
        self.__back_button.configure(command=self.__command_back)
        self.__back_button.pack(padx=(0, 230), pady=(5, 0))

        self.pack(padx=35, pady=35)
        
        # build widgets' view
        self.__excel_file_combo_box = customtkinter.CTkComboBox(master=self, values=[file for file in os.listdir(
            os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "..", "assets"))
            if ".xls" in file])

        self.__excel_file_combo_box.set("")
        self.__excel_file_combo_box.grid(row=0, column=1, sticky="ew", padx=(10, 30), pady=30)

        self.__build_labels()
        self.__build_entries()

        analysis_button = customtkinter.CTkButton(master=self, command=self.__command_analysis,
                                                  text=Settings.get_instance().get_text("DuplicateAnalysisView", "analysisButton"))
        analysis_button.grid(row=4, column=0, columnspan=2, pady=30)



    # METHODS
    def __build_labels(self) -> None:
        """
        SUMMARY
        -------
        This private method is called only in the constructor and is used to create all labels of the view.
        """
        excel_file_label = customtkinter.CTkLabel(master=self, text=Settings.get_instance().get_text("DuplicateAnalysisView", "fileLabel"))
        excel_file_label.grid(row=0, column=0, padx=(30, 10), pady=30)

        letter_column_label = customtkinter.CTkLabel(master=self, text=Settings.get_instance().get_text("DuplicateAnalysisView", "letterColumnLabel"))
        letter_column_label.grid(row=1, column=0, padx=(30, 10), pady=10)

        start_row_label = customtkinter.CTkLabel(master=self, text=Settings.get_instance().get_text("DuplicateAnalysisView", "firstRowLabel"))
        start_row_label.grid(row=2, column=0, padx=(30, 10), pady=10)

        end_row_label = customtkinter.CTkLabel(master=self, text=Settings.get_instance().get_text("DuplicateAnalysisView", "lastRowLabel"))
        end_row_label.grid(row=3, column=0, padx=(30, 10), pady=10)
    

    def __build_entries(self) -> None:
        """
        SUMMARY
        -------
        This private method is called only in the constructor and is used to create all entries to get the user input data.
        """
        self.__letter_column_entry = customtkinter.CTkEntry(master=self)
        self.__letter_column_entry.grid(row=1, column=1, padx=(10, 30), pady=10)

        self.__start_row_entry = customtkinter.CTkEntry(master=self)
        self.__start_row_entry.grid(row=2, column=1, padx=(10, 30), pady=10)

        self.__end_row_entry = customtkinter.CTkEntry(master=self)
        self.__end_row_entry.grid(row=3, column=1, padx=(10, 30), pady=10)

    
    
    # BUTTONS FUNCTION
    def __command_back(self) -> None:
        """
        SUMMARY
        -------
        This private method is the function linked with the 'back to menu' button when it pressed.
        It destroy this current view and rebuild a new home view.
        """
        self.__back_button.destroy()
        clear_frame(self)
        self.__app.change_view('HOME')


    def __command_analysis(self) -> None:
        """
        SUMMARY
        -------
        This private method is the function linked with the 'analysis' button when it pressed.
        It start the analysis of the duplicates in the excel file.
        """
        if not check_file(self.__excel_file_combo_box.get()):
            messagebox.showerror("AB Conseil application error", Settings.get_instance().get_text("MessageBoxError", "excelFileExists").format(self.self.__excel_file_combo_box.get()))
            return None

        if ".xls" not in self.__excel_file_combo_box.get():
            messagebox.showerror("AB Conseil application error", Settings.get_instance().get_text("MessageBoxError", "fileNotAnExcelFile").format(self.self.__excel_file_combo_box.get()))
            return None


        nb_duplicates = check_duplicates(self.__excel_file_combo_box.get(),
                                         self.__letter_column_entry.get().upper(),
                                         int(self.__start_row_entry.get()),
                                         int(self.__end_row_entry.get()))

        messagebox.showinfo("AB Conseil application", Settings.get_instance().get_text("DuplicateAnalysisView", "nbDuplicatesMessage").format(nb_duplicates))
