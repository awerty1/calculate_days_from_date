import os
from datetime import date


def create_output_filename():
    """
    Создает уникальное имя файла для вывода, основываясь на текущей дате.
    Если файл уже существует, добавляет суффикс, чтобы создать уникальное имя файла.
    """
    # Get the current date
    current_date = date.today()
    # Format the date as 'YYYY-MM-DD'
    date_str = current_date.strftime('%Y-%m-%d')
    # Create the directory if it doesn't exist
    directory = f'Dates_from_history/{date_str}'
    os.makedirs(directory, exist_ok=True)
    # Create the filename with the date included
    filename = f'{directory}/output_{date_str}.txt'
    # create suffix i++ if file exist
    suffix = 1
    while os.path.exists(filename):
        filename = f'{directory}/output_{date_str}_{suffix}.txt'
        suffix += 1
    return filename
