# import os
# import subprocess
# import logging

# def setup_logger():
#     # Create and configure the logger
#     logger = logging.getLogger(__name__)
#     logger.setLevel(logging.INFO)

#     # Create a file handler and set the logging level
#     log_file = os.path.join(os.getcwd(), "organize_rar_files.log")
#     file_handler = logging.FileHandler(log_file)
#     file_handler.setLevel(logging.INFO)

#     # Create a formatter and add it to the file handler
#     formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#     file_handler.setFormatter(formatter)

#     # Add the file handler to the logger
#     logger.addHandler(file_handler)

#     return logger

# def organize_rar_files(folder_path, logger):
#     try:
#         # Get a list of all files in the folder
#         all_files = os.listdir(folder_path)

#         # Dictionary to store files based on their extensions
#         files_by_extension = {}

#         # Group files by extension
#         for file in all_files:
#             _, extension = os.path.splitext(file)
#             extension = extension[1:]
#             if extension not in files_by_extension:
#                 files_by_extension[extension] = []
#             files_by_extension[extension].append(file)

#         # Create a new folder for organized RAR files
#         organized_folder = os.path.join(folder_path, "Organized_RAR_Files")
#         os.makedirs(organized_folder, exist_ok=True)

#         # Create RAR files and organize them into separate folders
#         for extension, files in files_by_extension.items():
#             extension_folder = os.path.join(organized_folder, extension.upper())
#             os.makedirs(extension_folder, exist_ok=True)

#             rar_filename = os.path.join(extension_folder, f"{extension}.rar")

#             # Construct the RAR command
#             rar_command = ['rar', 'a', rar_filename] + files

#             # Execute the RAR command
#             subprocess.run(rar_command, cwd=folder_path)

#         logger.info("RAR files organized successfully!")

#     except Exception as e:
#         logger.error(f"An error occurred: {str(e)}")

# if __name__ == "__main__":
#     # Provide the path to the folder containing files
#     folder_path = r"C:\Users\dipesh.kumar\Desktop\New folder"

#     # Set up the logger
#     logger = setup_logger()

#     # Call the function with the logger
#     organize_rar_files(folder_path, logger)

import logging

class logger:
    def log(self,message):
        raise NotImplementedError("Subclasses must implement the log method")
    
class FileLogger(logger):
    def __init__(self,filename):
        self.filename=filename
    
    def log(self,message):
        with open(self.filename,'a') as file:
            file.write(f"{message}\n")

class ConsoleLogger(logger):
    def log(self,message):
        print(message)

#example
file_logger=FileLogger("log.txt")
console_logger=ConsoleLogger()

file_logger.log("This message will be logged to a file.")
console_logger.log("This message will be logged to the console.")

