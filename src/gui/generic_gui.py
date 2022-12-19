import customtkinter



def clear_widgets(container: customtkinter.CTkFrame) -> None:
    """
    SUMMARY
    -------
    This function clear all widgets on the container passed as parameter.

    ARGUMENTS
    ---------
        container : customtkinter.CTkFrame
            The container that we want clean.
    """
    for widget in container.winfo_children():
        widget.destroy()
