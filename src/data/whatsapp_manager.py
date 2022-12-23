import time
import pyautogui
import webbrowser
from platform import system
from urllib.parse import quote
import customtkinter

from data.settings import Settings
from data.excel_utils import *



def launch_messages_wave(view: customtkinter.CTk, phone_number_parameter: tuple[str, int, int]) -> None:
    """
    SUMMARY
    -------
    This function send the message of the user to each number in the excel file informed.

    ARGUMENTS
    ---------
        - view : customtkinter.CTk
            The DraftingAdvertisingView to get some view data.
        - phone_number_parameter : tuple[str, int, int]
            The key parameter which represents the phone number parameter in the format
            (letter phone column => (first row, last row))
    """

    # open whatsapp for user to login by scanning qr-code. (wait 30s)
    try:
        webbrowser.open("https://web.whatsapp.com")
        time.sleep(30)
    except webbrowser.Error:
        return

    # close tab window for user to login
    __close_tab()

    # for each line in the excel file
    for row in range(phone_number_parameter[1], phone_number_parameter[2] + 1):
        final_message = __decrypted_message(view.get_excel_file(), view.get_message(), view.get_parameters(), row)
        phone_number = get_cell_data(view.get_excel_file(), phone_number_parameter[0], row)

        # verifications of the phone number data on the excel file
        if phone_number is None:
            continue
        if Settings.get_instance().get_phone_format() == "06":
            phone_number = "+33" + phone_number[1:]

        # open Whatsapp and wait 9s to allow time to load the page
        webbrowser.open(f"https://web.whatsapp.com/send?phone={phone_number}&text={quote(final_message)}")
        time.sleep(9)

        # click on screen center
        width, height = pyautogui.size()
        pyautogui.click(width / 2, height / 2)
        time.sleep(1)

        # press enter to send the message
        pyautogui.press("enter")
        
        # close the window 2s after
        __close_tab()


def get_all_messages_parameters(message_crypted: str) -> list[str]:
    """
    SUMMARY
    -------
    This function allows to get all parameters name in the message writes by the user.

    ARGUMENTS
    ---------
        - message_crypted : str
            The message writes by the user.

    Returns:
    list[str]: The list of all parameters name.
    None: If we have a problem with the numbers of brackets open and close.
    """
    index_brackets_open = [i for i, letter in enumerate(message_crypted) if letter == '{']
    index_brackets_close = [i for i, letter in enumerate(message_crypted) if letter == '}']

    if len(index_brackets_open) != len(index_brackets_close):
        return None
    
    parameters = []

    for i in range(len(index_brackets_open)):
        parameters.append(message_crypted[index_brackets_open[i] + 1:index_brackets_close[i]])
    
    return parameters


def __decrypted_message(excel_file_name: str, message_crypted: str, parameters: dict[str, tuple[str, str]], row: int) -> str:
    """
    SUMMARY
    -------
    This private function decryptes the message encoded with parameters for a specific row in the excel file.

    ARGUMENTS
    ---------
        - excel_file_name : str
            The name of the excel file.
        - message_crypted : str
            The message encoded with parameters.
        - parameters : dict[str, tuple[str, str]]
            List of all parameters in the format (parameter name => (default value, letter column)).
        - row : int
            The row of the current message.

    RETURNS
    -------
    str: The message decrypted to send on whatsapp.
    """

    # get positions of all brackets in the message
    index_brackets_open = [i for i, letter in enumerate(message_crypted) if letter == '{']
    index_brackets_close = [i for i, letter in enumerate(message_crypted) if letter == '}']

    # no parameters in the message
    if len(index_brackets_open) == 0:
        return message_crypted

    # get parameters value of this row
    parameters_value = get_row_data(excel_file_name, parameters, row)

    # add message part before the first parameter
    final_message = message_crypted[:index_brackets_open[0]]

    for i in range(len(index_brackets_open)):
        # substr to get the parameter name
        param = message_crypted[index_brackets_open[i] + 1:index_brackets_close[i]]

        # add parameter value
        final_message += parameters_value[param]

        # if it's not the last parameter
        if i < len(index_brackets_open) - 1:
            # add message content between the current parameter and the next. 
            final_message += message_crypted[index_brackets_close[i] + 1:index_brackets_open[i + 1]]
        else:
            # add final content of the message after the last parameter
            final_message += message_crypted[index_brackets_close[-1] + 1:]

    return final_message


def __close_tab(wait_time: int = 2) -> None:
    """
    SUMMARY
    -------
    Closes the Currently Opened Browser Tab
    """
    time.sleep(wait_time)

    if system().lower() in ("windows", "linux"):
        pyautogui.hotkey("ctrl", "w")
    elif system().lower() == "darwin":
        pyautogui.hotkey("command", "w")
    else:
        return None
