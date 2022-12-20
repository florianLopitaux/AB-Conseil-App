import pywhatkit.whats as pywhats
import customtkinter

from data.settings import Settings
from data.excel_utils import *



def launch_messages_wave(view: customtkinter.CTk, phone_number_parameter: tuple[str, int, int]) -> None:
    for row in range(phone_number_parameter[1], phone_number_parameter[2] + 1):
        final_message = __decrypted_message(view.get_excel_file(), view.get_message(), view.get_parameters(), row)
        phone_number = get_cell_data(view.get_excel_file(), phone_number_parameter[0], row)

        if phone_number is None:
            continue

        if Settings.get_instance().get_phone_format() == "06":
            phone_number = "+33" + phone_number[1:]

        pywhats.sendwhatmsg_instantly(phone_number, final_message)


def __decrypted_message(excel_file_name: str, message_crypted: str, parameters: dict[str, tuple[str, str]], row: int) -> str:
    # get positions of all brackets in the message
    index_brackets_open = [i for i, letter in enumerate(message_crypted) if letter == '{']
    index_brackets_close = [i for i, letter in enumerate(message_crypted) if letter == '}']

    # no parameters in the message
    if len(index_brackets_open) == 0:
        return message_crypted

    # add message part before the first parameter
    final_message = message_crypted[:index_brackets_open[0]]

    for i in range(len(index_brackets_open)):
        # substr to get the parameter name
        param = message_crypted[index_brackets_open[i] + 1:index_brackets_close[i]]
        # get the parameter value in the excel file
        cell_data = get_cell_data(excel_file_name, parameters[param][1], row)

        # no value in the excel file
        if cell_data is None:
            # default parameter value
            final_message += parameters[param][0]
        else:
            final_message += cell_data

        # if it's not the last parameter
        if i < len(index_brackets_open) - 1:
            # add message content between the current parameter and the next. 
            final_message += message_crypted[index_brackets_close[i] + 1:index_brackets_open[i + 1]]
            
    # add final content of the message after the last parameter
    final_message += message_crypted[index_brackets_close[-1] + 1:]

    return final_message
