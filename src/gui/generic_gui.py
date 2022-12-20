import customtkinter



def clear_frame(container: customtkinter.CTkFrame) -> None:
    """
    SUMMARY
    -------
    This function clear all widgets on the container passed as parameter and destroy them.

    ARGUMENTS
    ---------
        - container : customtkinter.CTkFrame
            The container that we want clean.
    """
    for widget in container.winfo_children():
        widget.destroy()
    
    container.destroy()


def create_red_button(container: customtkinter.CTkFrame, button_text: str) -> customtkinter.CTkButton:
    """
    SUMMARY
    -------
    This method genrates and return a custom red button (typically used for a negative button).

    ARGUMENTS
    ---------
        - container : customtkinter.CTkFrame
            The frame that contains the button.
        - button_text : str
            The text that we want inside on the button.

    RETURNS
    -------
    customtkinter.CTkButton: the generated button requested.
    """
    return customtkinter.CTkButton(master=container, text=button_text, fg_color="#B22222", hover_color="#F08080")


def create_green_button(container: customtkinter.CTkFrame, button_text: str) -> customtkinter.CTkButton:
    """
    SUMMARY
    -------
    This method genrates and return a custom green button (typically used for a positive button).

    ARGUMENTS
    ---------
        - container : customtkinter.CTkFrame
            The frame that contains the button.
        - button_text : str
            The text that we want inside on the button.

    RETURNS
    -------
    customtkinter.CTkButton: the generated button requested.
    """
    return customtkinter.CTkButton(master=container, text=button_text, fg_color="#32CD32", hover_color="#7CFC00")
