import os
import subprocess
import asyncio

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

async def organize_files_by_extension(organized_folder, files_by_extension):
    for extension, files in files_by_extension.items():
        extension_folder = os.path.join(organized_folder, extension.upper())
        os.makedirs(extension_folder, exist_ok=True)

        rar_filename = os.path.join(extension_folder, f"{extension}.rar")

        yield rar_filename, files

async def create_rar(rar_filename, files, folder_path):
    rar_command = ['rar', 'a', rar_filename] + files
    process = await asyncio.create_subprocess_exec(*rar_command, cwd=folder_path)
    await process.communicate()

async def organize_rar_files_generator(folder_path):
    all_files = get_all_files(folder_path)
    files_by_extension = group_files_by_extension(all_files)
    organized_folder = create_organized_folder(folder_path)

    yield files_by_extension
    yield organized_folder

    try:
        async for rar_filename, files in organize_files_by_extension(organized_folder, files_by_extension):
            yield rar_filename, files
    except StopIteration:
        pass

async def organize_rar_files(folder_path):
    generator = organize_rar_files_generator(folder_path)

    try:
        files_by_extension = await generator.__anext__()
        organized_folder = await generator.__anext__()

        async for rar_filename, files in generator:
            await create_rar(rar_filename, files, folder_path)

        print("RAR files organized successfully!")

    except StopAsyncIteration:
        print("No files to organize.")

# Provide the path to the folder containing files
async def main():
    # Provide the path to the folder containing files
    folder_path = r"C:\Users\dipesh.kumar\Desktop\New folder"
    await organize_rar_files(folder_path)

# Run the event loop
if __name__ == "__main__":
    asyncio.run(main())
