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
    index_brackets_open = [i for i, letter in enumerate(message_crypted) if letter == '{']
    index_brackets_close = [i for i, letter in enumerate(message_crypted) if letter == '}']

    if len(index_brackets_open) == 0:
        return message_crypted

    finalMessage = message_crypted[:index_brackets_open[0]]

    for i in range(len(index_brackets_open)):
        param = message_crypted[index_brackets_open[i] + 1:index_brackets_close[i]]
        cell_data = get_cell_data(excel_file_name, parameters[param][1], row)

        if cell_data is None:
            finalMessage += parameters[param][0]
        else:
            finalMessage += cell_data

        if i == len(index_brackets_open) - 1:
            break
        else:
            finalMessage += message_crypted[index_brackets_close[i] + 1:index_brackets_open[i + 1]]
    
    finalMessage += message_crypted[index_brackets_close[-1] + 1:]
    return finalMessage
