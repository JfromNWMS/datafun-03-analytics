"""
Process a CSV file on 2020 Happiness ratings by country to analyze the `Ladder score` column and save statistics.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import sys

# Import from external packages
from torch import device
from torch import tensor
from torch import corrcoef
from torch import linalg
from torch import cuda

from pandas import concat
from pandas import read_csv
from pandas import DataFrame

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

def principal_component_analysis(file_path: pathlib.Path) -> tuple:
    """Analyze the Ladder score column to calculate min, max, mean, and stdev."""
    try:
        data = read_csv(file_path, index_col=0, usecols=lambda x: x != 'Regional indicator')
        gpu_or_cpu = device('cuda' if cuda.is_available() else 'cpu')
        # torch.tensor() creates tensor from rows of pandas dataframe and is allocated
        # to GPU memory if cuda is available.
        data_tensor = tensor(data.values).to(gpu_or_cpu)
        # torch.corrcoef() creates Pearson correlation coefficient matrix from the tensors (rows of data).
        pearson_corr = corrcoef(data_tensor)
        # torch.linalg.eigh() returns indexed tensors of eigenvalues and eigenvectors
        # of the input matrix, where the eigenvalues are in ascending order. 
        eigenvalues, eigenvectors = linalg.eigh(pearson_corr)
        # Creating pandas dataframe from tensors as rows then transposing them to have eigenvectors as columns.
        # Pandas .concat() then used to merge the eigenvalues above their corresponding eigenvectors.
        eigen_info = concat([DataFrame(eigenvalues.to('cpu')).T, DataFrame(eigenvectors.to('cpu')).T])
        return (eigen_info, gpu_or_cpu)
    
    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")

def process_csv_file():
    """Read a CSV file, analyze Ladder score, and save the results."""
    
    # TODO: Replace with path to your CSV data file
    input_file = pathlib.Path(FETCHED_DATA_DIR, "2020_happiness.csv")
    
    # TODO: Replace with path to your CSV processed file
    output_txt = pathlib.Path(PROCESSED_DIR, "happiness_eigen_summary.txt")
    output_csv = pathlib.Path(PROCESSED_DIR, "happiness_eigen_info.csv")
    
    # TODO: Call your new function to process YOUR CSV file
    # TODO: Create a new local variable to store the result of the function call
    eigen_info, gpu_or_cpu = principal_component_analysis(input_file)

    # Create the output directory if it doesn't exist
    output_txt.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_txt.open('w') as file:

        file.write(f"{input_file} eigen summary with device: {gpu_or_cpu}\n")
        file.write(f"Least 5 eigenvalues: {", ".join(f'{x:.5e}' for x in eigen_info.iloc[0,:5])}\n")
        file.write(f"Greatest 5 eigenvalues: {", ".join(f'{x:.5e}' for x in eigen_info.iloc[0,-5:])}\n")

    # Writes eigen_info to CSV.
    eigen_info.to_csv(output_csv, header=False, index=False)
    # Log the processing of the CSV file
    logger.info(f"Processed CSV file: {input_file}, summary saved to: {output_txt} and eigen info save to: {output_csv}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    process_csv_file()
    logger.info("CSV processing complete.")