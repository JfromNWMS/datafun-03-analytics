"""
Process a text file to count occurrences of the words "Romeo" and "Juliet" in the same line for all lines in the file and save the result.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import sys

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

def count_word_occurrences_by_line(file_path: pathlib.Path, word_list: list) -> int:
    """Count the number of lines in a text file that contain all of the words in a list (case-insensitive).
    Args:
         file_path (pathlib.path): File path.
         word_list (list): List of str's."""
    try:
        with file_path.open('r') as file:  
            word_list = [word.lower() for word in word_list]
            # A sum of one boolean per line over all lines in the text file.  
            # True will be returned for the line if the line contains all of the words in the list.
            # This sum yields the total number of lines in the file that contain all words in a list.
            number_lines_all: int = sum(all(word in line.lower() for word in word_list) for line in file)
            return number_lines_all
        
    except Exception as e:
        logger.error(f"Error reading text file: {e}")

def process_text_file():
    """Read a text file, count occurrences of a line containing all words in a list for the file, and save the result."""
    input_file = pathlib.Path(FETCHED_DATA_DIR, "romeo.txt")
    output_file = pathlib.Path(PROCESSED_DIR, "text_word_list_count_by_line.txt")

    word_list: list = ["Romeo","Juliet"]
    word_count: int = count_word_occurrences_by_line(input_file, word_list)

    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open('w') as file:
        file.write(f"Occurrences of '{"' and '".join(word_list)}': {word_count}\n")
    
    logger.info(f"Processed text file: {input_file}, Word count saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting text processing...")
    process_text_file()
    logger.info("Text processing complete.")