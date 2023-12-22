import os
import subprocess

def organize_rar_files(folder_path):
    
    # Get a list of all files in the folder
    all_files = os.listdir(folder_path)

    # Dictionary to store files based on their extensions
    files_by_extension = {}

    # Group files by extension
    for file in all_files:
        _, extension = os.path.splitext(file)
        extension = extension[1:]
        if extension not in files_by_extension:
            files_by_extension[extension] = []
        files_by_extension[extension].append(file)

    # Create a new folder for organized RAR files
    organized_folder = os.path.join(folder_path, "Organized_RAR_Files")
    os.makedirs(organized_folder, exist_ok=True)

    # Create RAR files and organize them into separate folders
    for extension, files in files_by_extension.items():
        extension_folder = os.path.join(organized_folder, extension.upper())
        os.makedirs(extension_folder, exist_ok=True)

        rar_filename = os.path.join(extension_folder, f"{extension}.rar")

        # Construct the RAR command
        rar_command = ['rar', 'a', rar_filename] + files

        # Execute the RAR command
        subprocess.run(rar_command, cwd=folder_path)

    print("RAR files organized successfully!")

# Provide the path to the folder containing files
folder_path = r"C:\Users\dipesh.kumar\Desktop\New folder"
organize_rar_files(folder_path)
