import os
import subprocess

def get_all_files(folder_path):
    return os.listdir(folder_path)

def group_files_by_extension(all_files):
    files_by_extension = {}
    for file in all_files:
        _, extension = os.path.splitext(file)
        extension = extension[1:]
        if extension not in files_by_extension:
            files_by_extension[extension] = []
        files_by_extension[extension].append(file)
    return files_by_extension

def create_organized_folder(folder_path):
    organized_folder = os.path.join(folder_path, "Organized_RAR_Files")
    os.makedirs(organized_folder, exist_ok=True)
    return organized_folder

def organize_files_by_extension(organized_folder, files_by_extension):
    for extension, files in files_by_extension.items():
        extension_folder = os.path.join(organized_folder, extension.upper())
        os.makedirs(extension_folder, exist_ok=True)

        rar_filename = os.path.join(extension_folder, f"{extension}.rar")

        yield rar_filename, files

def create_rar(rar_filename, files, folder_path):
    rar_command = ['rar', 'a', rar_filename] + files
    subprocess.run(rar_command, cwd=folder_path)

def organize_rar_files_generator(folder_path):
    all_files = get_all_files(folder_path)
    files_by_extension = group_files_by_extension(all_files)
    organized_folder = create_organized_folder(folder_path)

    yield files_by_extension
    yield organized_folder

    try:
        files_generator = organize_files_by_extension(organized_folder, files_by_extension)
        yield from files_generator
    except StopIteration:
        pass

def organize_rar_files(folder_path):
    generator = organize_rar_files_generator(folder_path)

    try:
        files_by_extension = next(generator)
        organized_folder = next(generator)

        for rar_filename, files in generator:
            create_rar(rar_filename, files, folder_path)

        print("RAR files organized successfully!")

    except StopIteration:
        print("No files to organize.")

# Provide the path to the folder containing files
folder_path = r"C:\Users\dipesh.kumar\Desktop\New folder"
organize_rar_files(folder_path)
