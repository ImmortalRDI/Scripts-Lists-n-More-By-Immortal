import os
import subprocess

def convert_and_resize_png(source_directory, destination_directory_144, destination_directory_64):
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.endswith(".png"):
                full_file_path = os.path.join(root, file)
                
                # Define the new file paths
                new_file_name_dds = os.path.splitext(file)[0] + ".DDS"
                new_file_path_dds = os.path.join(destination_directory_144, new_file_name_dds)

                new_file_name_png = os.path.splitext(file)[0] + ".png"
                new_file_path_png = os.path.join(destination_directory_64, new_file_name_png)
                
                # Call ImageMagick to convert and resize the file to 144x144 and save as DDS
                subprocess.run(["magick", "convert", full_file_path, "-resize", "144x144", new_file_path_dds])
                
                # Call ImageMagick to resize the file to 64x64 and save as PNG
                subprocess.run(["magick", "convert", full_file_path, "-resize", "64x64", new_file_path_png])

# Example usage
source_directory = 'path\\to\\your\\icons'
destination_directory_144 = 'path\\to\\your\\controller\\icons\\folder'
destination_directory_64 = 'path\\you\\want\\64x64\\images\\for\\atlas'
convert_and_resize_png(source_directory, destination_directory_144, destination_directory_64)