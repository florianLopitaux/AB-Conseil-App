import os
from openpyxl import load_workbook
from openpyxl.worksheet.worksheet import Worksheet



def check_file(file_name: str) -> bool:
    return os.path.exists(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "..", "assets", file_name))


def get_cell_data(excel_file_name: str, letter_column: str, row: int):
    wb = load_workbook(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "..", "assets", excel_file_name))
    ws = wb.active

    cell_data = ws[letter_column + str(row)]

    wb.close()
    return cell_data.value


def get_row_data(excel_file_name: str, parameters: dict[str, tuple[str, str]], row: int) -> dict[str, str]:
    wb = load_workbook(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "..", "assets", excel_file_name))
    ws = wb.active

    params_value = dict()
    for param_name, values in parameters.items():
        current_data = __get_cell_data(ws, values[1], row)

        if current_data is None:
            params_value[param_name] = values[0]
        else:
            params_value[param_name] = current_data

    wb.close()
    return params_value


def __get_cell_data(ws: Worksheet, letter_column:str, row: int) -> str:
    return ws[letter_column + str(row)].value
