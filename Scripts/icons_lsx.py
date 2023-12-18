import os
import xml.etree.ElementTree as ET

def update_lsx_file(image_directory, lsx_file_path):
    # Read image names in sorted order
    image_names = sorted([f for f in os.listdir(image_directory) if f.endswith('.DDS')])

    # Load and parse the .lsx file
    tree = ET.parse(lsx_file_path)
    root = tree.getroot()

    # Find all the <node id="IconUV"> elements and update MapKey values
    icon_nodes = root.findall(".//node[@id='IconUV']")
    for i, node in enumerate(icon_nodes):
        if i < len(image_names):
            mapkey_attrib = node.find("./attribute[@id='MapKey']")
            if mapkey_attrib is not None:
                # Extracting the base name without extension and any preceding path
                new_mapkey = os.path.splitext(image_names[i])[0]
                mapkey_attrib.set('value', new_mapkey)
        else:
            break  # Stop if there are no more images

    # Save the updated .lsx file
    with open(lsx_file_path, 'wb') as file:
        file.write(b'<?xml version="1.0" encoding="utf-8"?>\n')
        tree.write(file, encoding='utf-8')

# Example usage
image_directory = 'Path\\to\\your\\icons'
lsx_file_path = 'path\\to\\your\\Icons.lsx'
update_lsx_file(image_directory, lsx_file_path)