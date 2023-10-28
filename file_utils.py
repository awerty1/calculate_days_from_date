import os
from datetime import date


def create_output_filename():
    """
    Create a unique output filename based on the current date.
    If the file already exists, append a suffix to create a unique filename.
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
