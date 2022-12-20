import os
from openpyxl import load_workbook



def check_file(file_name: str) -> bool:
    return os.path.exists(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "..", "assets", file_name))


def get_cell_data(excel_file_name: str, letter_column:str, row: int) -> str:
    wb = load_workbook(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "..", "assets", excel_file_name))
    ws = wb.active

    cell_data = ws[letter_column + str(row)]

    wb.close()
    return cell_data.value
