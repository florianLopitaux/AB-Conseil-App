from typing import Self
import customtkinter


class Settings:
    # STATIC ATTRIBUTE
    __INSTANCE = None


    # CONSTRUCTOR
    def __init__(self):
        if (Settings.__INSTANCE is None):
            self.__appearance_mode, self.__color_theme = self.__load_configuration()
    

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


    # METHODS
    def __load_configuration() -> tuple[str, str]:
        pass


    # STATIC METHODS
    @staticmethod
    def get_instance() -> Self:
        if (Settings.__INSTANCE is None):
            return Settings()
        else:
            return Settings.__INSTANCE
