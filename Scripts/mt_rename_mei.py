import os
import sys
import shutil
import xml.etree.ElementTree as ET

def backup_file(file_path, backup_directory):
    os.makedirs(backup_directory, exist_ok=True)
    filename = os.path.basename(file_path)
    backup_path = os.path.join(backup_directory, filename)
    shutil.copyfile(file_path, backup_path)
    print(f"Backup created: {backup_path}")
    return backup_path

def mt_rename_mei(root_directory, backup_directory):
    backup_paths = []
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Backup original file
                backup_path = backup_file(file_path, backup_directory)
                backup_paths.append(backup_path)

                # Parse XML-like file
                tree = ET.parse(file_path)
                root_element = tree.getroot()

                # Find the attribute with id="Name" and type="LSString"
                for elem in root_element.iter():
                    if 'id' in elem.attrib and 'type' in elem.attrib:
                        if elem.attrib['id'] == 'Name' and elem.attrib['type'] == 'LSString':
                            value = elem.attrib.get('value', None)
                            if value:
                                # Extract filename and extension
                                filename, file_extension = os.path.splitext(file)
                                new_file_name = f"{value}{file_extension}"  # Append .lsf without changing extension
                                new_file_path = os.path.join(root, new_file_name)
                                os.rename(file_path, new_file_path)
                                print(f"File renamed to: {new_file_name}")
                                break  # Stop after renaming the file

            except Exception as e:
                print(f"An error occurred: {e}")

    return backup_paths

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mt_rename_mei.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        backup_dir = r"your\\backup\\directory\\here"
        mt_rename_mei(directory_path, backup_dir)