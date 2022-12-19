from typing import Self
import os
import json
import customtkinter



class Settings:
    """
    SUMMARY
    -------
    This class stored the data settings of the application.
    It load and register data from a json file calld 'app-configuration.json' in the 'assets' folder.
    Also, this class uses the singleton design pattern to instantiate just once and get the object with static method.

    METHODS
    -------
        GETTERS
        -------
        - get_appearance_mode() -> str
        - get_color_theme() -> str
        - get_phone_format() -> str

        SETTERS
        -------
        - set_appearance_mode(appearance_mode: str) -> None
        - set_color_theme(color_theme: str) -> None
        - set_phone_format(phone_format: str) -> None

        STATIC
        ------
        - get_instance() -> Self
    """
    # STATIC ATTRIBUTE
    __INSTANCE = None
    __PATH_JSON_CONFIGURATION_FILE = os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "..", "assets", "app-configuration.json")


    # CONSTRUCTOR
    def __init__(self):
        """
        SUMMARY
        -------
        This constructor loads and reads the data stored on the json configuration file.
        If the method can't open the file or decode the content, it raises an error with a message box to the user.
        """
        if (Settings.__INSTANCE is None):
            self.__json_configuration = None

            try:
                with open(Settings.__PATH_JSON_CONFIGURATION_FILE) as json_file:
                    self.__json_configuration =  json.load(json_file)

            except FileNotFoundError:
                print("Error ! Can't open the json configuration file")
            except json.JSONDecodeError:
                print("Error ! Can't read/decode json configuration file")

            customtkinter.set_appearance_mode(self.__json_configuration['appearance_mode'])
            customtkinter.set_default_color_theme(self.__json_configuration['color_theme'])



    # GETTERS
    def get_appearance_mode(self) -> str:
        """
        SUMMARY
        -------
        This method is the getter to the 'appearance_mode' attribute.
        The attribute stores the string value of the currently appearance mode of the application.

        RETURNS
        -------
        str: The currently appearance mode of the application.
        """
        return self.__json_configuration['appearance_mode']


    def get_color_theme(self) -> str:
        """
        SUMMARY
        -------
        This method is the getter to the 'color_theme' attribute.
        The attribute stores the string value of the currently color theme of the application.

        RETURNS
        -------
        str: The currently color theme of the application.
        """
        return self.__json_configuration['color_theme']
    

    def get_phone_format(self) -> str:
        """
        SUMMARY
        -------
        This method is the getter to the 'phone_format' attribute.
        The attribute stores the string value of the currently phone format of the application.

        RETURNS
        -------
        str: The currently phone format of the application.
        """
        return self.__json_configuration['phone_format']



    # SETTERS
    def set_appearance_mode(self, appearance_mode: str) -> None:
        """
        SUMMARY
        -------
        This method is the setter to the 'appearance_mode' attribute.
        The setter stores also the new value choose on the json configuration file.
        The argument has only 3 possibilities : 'System', 'Dark' and 'Light'.
        If the argument doesn't 3 of them, an AssertionError is thrown.

        ARGUMENTS
        ---------
            appearance_mode : str
                The appearance of the application that we want applied.
        """
        assert appearance_mode in ["System", "Dark", "Light"], "Error ! Appearance mode: '" + appearance_mode + "' doesn't exist !"

        self.__json_configuration['appearance_mode'] = appearance_mode
        self.__saveData()

        customtkinter.set_appearance_mode(appearance_mode)


    def set_color_theme(self, color_theme: str) -> None:
        """
        SUMMARY
        -------
        This method is the setter to the 'color_theme' attribute.
        The setter stores also the new value choose on the json configuration file.
        The argument has only 2 possibilities : 'blue', 'green'.
        If the argument doesn't 2 of them, an AssertionError is thrown.

        ARGUMENTS
        ---------
            color_theme : str
                The color theme of the application that we want applied.
        """
        assert color_theme in ["blue", "green"], "Error ! Theme color: '" + color_theme + "' doesn't exist !"

        self.__json_configuration['color_theme'] = color_theme
        self.__saveData()

        customtkinter.set_default_color_theme(color_theme)


    def set_phone_format(self, phone_format: str) -> None:
        """
        SUMMARY
        -------
        This method is the setter to the 'phone_format' attribute.
        The setter stores also the new value choose on the json configuration file.
        The argument has only 2 possibilities : '06', '+33'.
        If the argument doesn't 2 of them, an AssertionError is thrown.

        ARGUMENTS
        ---------
            phone_format : str
                The phone format of the application that we want applied.
        """
        assert phone_format in ["06", "+33"], "Error ! Phone format: '" + phone_format + "' doesn't exist !"

        self.__json_configuration['phone_format'] = phone_format
        self.__saveData()



    # METHODS
    def __saveData(self) -> None:
        """
        SUMMARY
        -------
        This private method is called by the setters to save new data on the json configuration file.
        If the method can't open the json configuration file, it raises an error with a message box to the user.
        """
        try:
            with open(Settings.__PATH_JSON_CONFIGURATION_FILE, 'w') as file_out:
                json.dump(self.__json_configuration, file_out)

        except FileNotFoundError:
            print("Error ! Can't open the json configuration file")



    # STATIC METHODS
    @staticmethod
    def get_instance() -> Self:
        """
        SUMMARY
        -------
        This static method allows to get the instance of the Settings class (see Singleton design pattern).

        RETURNS
        -------
        Settings: The instance of the class.
        """
        if (Settings.__INSTANCE is None):
            return Settings()
        else:
            return Settings.__INSTANCE
