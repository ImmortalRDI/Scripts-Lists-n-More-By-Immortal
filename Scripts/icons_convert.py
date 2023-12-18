import os
import subprocess

def convert_png_to_dds(source_directory, destination_directory):
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.endswith(".png"):
                full_file_path = os.path.join(root, file)
                # Define the new file path with the DDS extension
                new_file_name = os.path.splitext(file)[0] + ".DDS"
                new_file_path = os.path.join(destination_directory, new_file_name)
                
                # Call ImageMagick to convert the file
                subprocess.run(["magick", "convert", full_file_path, new_file_path])

# Example usage
source_directory = 'path\\to\\your\\png\\icons'
destination_directory = 'path\\you\\want\\your\\.DDS\\icons'
convert_png_to_dds(source_directory, destination_directory)