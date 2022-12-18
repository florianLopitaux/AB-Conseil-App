import customtkinter


class Settings:
    # CONSTRUCTOR
    def __init__(self):
        pass
    

    # GETTERS
    def get_appearance_mode(self) -> str:
        return self.__appearance_mode

    def get_color_theme(self) -> str:
        return self.__color_theme
    

    # SETTERS
    def set_appearance_mode(self, appearance_mode: str) -> None:
        assert appearance_mode in ["System", "Dark", "Light"], "Error ! Appearance mode: '" + appearance_mode + "' doesn't exist !"

        self.__appearance_mode = appearance_mode
        customtkinter.set_appearance_mode(appearance_mode)

    def set_color_theme(self, color_theme: str) -> None:
        assert color_theme in ["blue", "green"], "Error ! Theme color: '" + color_theme + "' doesn't exist !"

        self.__color_theme = color_theme
        customtkinter.set_default_color_theme(color_theme)
