import os
import sys

def mt_rename_lsfx(root_directory):
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if file.endswith('.lsx') and not file.endswith('.lsf.lsx'):  # Check if file doesn't have .lsf in name
                file_path = os.path.join(root, file)
                directory, full_filename = os.path.split(file_path)
                file_name, file_extension = os.path.splitext(full_filename)

                new_file_name = f"{file_name}.lsf{file_extension}"
                new_file_path = os.path.join(directory, new_file_name)

                try:
                    if not os.path.exists(new_file_path):  # Check if the file with .lsf doesn't exist
                        os.rename(file_path, new_file_path)
                        print(f"File renamed as: {new_file_name}")
                    else:
                        print(f"File with .lsf name already exists: {new_file_name}")
                        os.rename(file_path, new_file_path)  # Overwrite existing file
                        print(f"File overwritten as: {new_file_name}")
                except Exception as e:
                    print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mt_rename_lsfx.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        mt_rename_lsfx(directory_path)
