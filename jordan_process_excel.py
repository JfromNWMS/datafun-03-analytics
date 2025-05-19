"""
Process an Excel file to count occurrences of a specific word in a column.

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import sys

# Import from external packages
import openpyxl

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

FETCHED_DATA_DIR: str = "data"
PROCESSED_DIR: str = "processed_data"

#####################################
# Define Functions
#####################################

def count_word_in_column(file_path: pathlib.Path, word: str) -> int:
    """Count the occurrences of a specific word in a given column of an Excel file."""
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        word = word.lower()
        # any() will return a single boolean if at least one cell in a row contains word.
        # any() is iterated over all rows in the sheet.
        # row_is_true is a list of booleans corresponding to the rows in the sheet.
        row_is_true: list = [any(word in str(cell.value).lower() for cell in row) for row in sheet.iter_rows()]
        # Sum all booleans in row_is_true to determine how many rows of sheet contain word.
        return sum(row_is_true)
        
    except Exception as e:
        logger.error(f"Error reading Excel file: {e}")

def process_excel_file():
    """Read an Excel file, count occurrences of 'GitHub' in a specific column, and save the result."""
    
    input_file = pathlib.Path(FETCHED_DATA_DIR, "Feedback.xlsx")
    output_file = pathlib.Path(PROCESSED_DIR, "excel_feedback_github_count.txt")

    word_to_count = "GitHub"
    word_count = count_word_in_column(input_file, word_to_count)
    
    # Write the results to the output file    
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:
        file.write(f"The number of rows '{word_to_count}' occurs in is: {word_count}\n")
    
    # Log the processing of the Excel file    
    logger.info(f"Processed Excel file: {input_file}, Rows that contain word count saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting Excel processing...")
    process_excel_file()
    logger.info("Excel processing complete.")