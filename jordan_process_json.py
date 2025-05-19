"""
Process a JSON file to count astronauts by spacecraft and save the result.

JSON file is in the format where people is a list of dictionaries with keys "craft" and "name".

{
    "people": [
        {
            "craft": "ISS",
            "name": "Oleg Kononenko"
        },
        {
            "craft": "ISS",
            "name": "Nikolai Chub"
        }
    ],
    "number": 2,
    "message": "success"
}

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import json
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

def count_astronauts_by_craft(file_path: pathlib.Path) -> dict:
    """Count the number of astronauts on each spacecraft from a JSON file."""
    try:
        with file_path.open('r') as file:

            astronaut_dictionary = json.load(file)  
            people_list: list = astronaut_dictionary.get("people", [])
            craft_counts_dictionary = {}

            for person_dictionary in people_list:  
                craft = person_dictionary.get("craft", "Unknown")
                craft_counts_dictionary[craft] = craft_counts_dictionary.get(craft, 0) + 1
            return craft_counts_dictionary
        
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {}

def process_json_file():
    """Read a JSON file, count astronauts by spacecraft, and save the result."""

    input_file: pathlib.Path = pathlib.Path(FETCHED_DATA_DIR, "astros.json")
    output_file: pathlib.Path = pathlib.Path(PROCESSED_DIR, "json_astronauts_by_craft.txt")
    
    craft_counts = count_astronauts_by_craft(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open('w') as file:
        file.write("Astronauts by spacecraft:\n")
        for craft, count in craft_counts.items():
            file.write(f"{craft}: {count}\n")
    
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")