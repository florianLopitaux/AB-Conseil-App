from typing import Self
import os
import json
import customtkinter


class Settings:
    # STATIC ATTRIBUTE
    __INSTANCE = None


    # CONSTRUCTOR
    def __init__(self):
        if (Settings.__INSTANCE is None):
            self.__appearance_mode, self.__color_theme = self.__load_configuration()

            customtkinter.set_appearance_mode(self.__appearance_mode)
            customtkinter.set_default_color_theme(self.__color_theme)
    

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
    def __load_configuration(self) -> tuple[str, str]:
        jons_file = None

        try:
            json_file = open(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "..", "assets", "app-configuration.json"))
        except OSError:
            print("Error ! Can't open the json configuration file")

        json_configuration = None

        try:
            json_configuration =  json.load(json_file)
        except json.JSONDecodeError:
            print("Error ! Can't read/decode json configuration file")

        json_file.close()
        return json_configuration['appearance_mode'], json_configuration['color_theme']


    # STATIC METHODS
    @staticmethod
    def get_instance() -> Self:
        if (Settings.__INSTANCE is None):
            return Settings()
        else:
            return Settings.__INSTANCE
