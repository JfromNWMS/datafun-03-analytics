# datafun-03-analytics
This project overviews data retrieval and processing from a url.  Four modules retrieve data from a desired url and write the data to file and four modules process those files for the four file types of csv, excel, json, and text.  Descriptionts of the modules broken into retrieval and processing groups are as follows:

Retrieval:

    jordan_get_csv.py:  Module contains the function fetch_csv_file(folder_name: str, filename: str, url: str), where fetch_csv_file() obtains a csv file from desired url and creates a folder named folder_name in the project directory and writes to csv file of name filename in that folder.
    Execute "PS> py jordan_get_csv.py" in powershell to fetch 2020_happiness.csv and write to data\2020_happiness.csv.  The main() function of the module can be modified or import and call the function passing desired args to function if another retrieval point or file write name/location is desired.

    jordan_get_excel.py:  Module contains the function fetch_excel_file(folder_name: str, filename: str, url: str), where fetch_excel_file() obtains a excel file from desired url and creates a folder named folder_name in the project directory and writes to excel file of name filename in that folder.
    Execute "PS> py jordan_get_excel.py" in powershell to fetch Feedback.xlsx and write to data\Feedback.xlsx.  The main() function of the module can be modified or import and call the function passing desired args to function if another retrieval point or file write name/location is desired.

    jordan_get_json.py:  Module contains the function fetch_json_file(folder_name: str, filename: str, url: str), where fetch_json_file() obtains a json file from desired url and creates a folder named folder_name in the project directory and writes to json file of name filename in that folder.
    Execute "PS> py jordan_get_json.py" in powershell to fetch astros.json and write to astros.json.  The main() function of the module can be modified or import and call the function passing desired args to function if another retrieval point or file write name/location is desired.

    jordan_get_text.py:  Module contains the function fetch_text_file(folder_name: str, filename: str, url: str), where fetch_text_file() obtains a text file from desired url and creates a folder named folder_name in the project directory and writes to text file of name filename in that folder.
    Execute "PS> py jordan_get_text.py" in powershell to fetch romeo.txt and write to romeo.txt.  The main() function of the module can be modified or import and call the function passing desired args to function if another retrieval point or file write name/location is desired.

Prcessing:

    jordan_process_csv.py: Module contains the function pearson_eigen_info(file_path: pathlib.Path) which creates a pearson correlation coefficient matrix by row and finds the eigenvectors and corresponding eigenvalues for the pearson matrix for a given file path passed as file_path arg. The function returns a two element tuple with the first elements being a pandas dataframe contianing the eigenvectors and corresponding eigenvalues and the second element being a str indicating whether the cpu or gpu was used for processing. Module contains function process_csv_file() which runs pearson_eigen_info() on data\happiness.csv and writes the eignvectors and eigenvalues to csv file processed_data\happiness_eigen_info.csv and writes device used, five greatest eigenvalues, and five least eigenvalues to text file processed_data\happiness_eigen_summary.txt. 
    Execute "PS> py jordan_process_csv.py" in powershell to call process_csv_file() on data\2020_happiness.csv.

    jordan_process_excel.py: Module contains the function count_rows_with_word(file_path: pathlib.Path, word: str) which counts the number of rows in the given excel file, passed in by arg file_path, which contain a given word that is passed to the function by arg word and returns the count as int.  Module also contains function process_excel_file() which calls count_rows_with_word() on data\Feedback.xlsx with word arg of 'GitHub' and writes the word to be counted and the number of rows it was counted in to a text file created at processed_data\excel_feedback_github_count.txt.
    Execute "PS> py jordan_process_excel.py" in powershell to call process_excel_file() on data\Feedback.xlsx.

    jordan_process_json.py: Module contains the function count_astronauts_by_craft(file_path: pathlib.Path) which takes in a json file path as arg file_path and counts the frequency of values that the 'craft' index contains within a dictionary over a list of dictionaries then returns a dictionary frequency table of the values.  Module also contain function process_json_file() which calls count_astronauts_by_craft() on data\astros.json and writes a frequency table to processed_data\json_astronauts_by_craft.txt.
    Execute "PS> py jordan_process_json.py" in powershell to call process_json_file() on data\astros.json.

    jordan_process_text.py: Module contains function count_word_occurrences_by_line(file_path: pathlib.Path, word_list: list) which counts the total number of lines that contain all words in the input arg list word_list in the text file located at path file_path arg and returns an int.  Module also contains function process_text_file() which calls count_word_occurrences_by_line() on data\romeo.txt for words "Romeo" and "Juliet" then writes the list of words and the count for the number of times they occured on every line of data\romeo.txt to processed_data\text_word_list_count_by_line.txt.
