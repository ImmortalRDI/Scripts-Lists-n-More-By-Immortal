import random
import string
import re
import xml.etree.ElementTree as ET
import xml.dom.minidom

def generate_unique_hid(existing_hids):
    while True:
        new_hid = 'h' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=36))  # 36 characters plus 'h'
        if new_hid not in existing_hids:
            return new_hid

def process_txt_and_create_xml(txt_file_path, xml_file_path):
    existing_hids = set()
    xml_root = ET.Element("contentList")

    with open(txt_file_path, 'r') as file:
        txt_lines = file.readlines()

    entry_name = ""
    for i, line in enumerate(txt_lines):
        if line.startswith('new entry'):
            entry_name = line.split('"')[1]  # Extract the entry name (e.g., INVISIBLE_EM_ARCANE)

        if "data \"DisplayName\"" in line or "data \"Description\"" in line:
            new_hid = generate_unique_hid(existing_hids)
            existing_hids.add(new_hid)

            # Update the line in the txt file
            line = re.sub(r'(data "(DisplayName|Description)" ")[^"]+;', f'\\1"{new_hid};', line)
            txt_lines[i] = line

            # Create XML content element
            content_element = ET.SubElement(xml_root, "content")
            content_element.set("contentuid", new_hid)
            content_element.set("version", "1")
            content_type = "DisplayName" if "DisplayName" in line else "Description"
            content_element.text = f"{entry_name} ({content_type})"

    # Save the modified txt file
    with open(txt_file_path, 'w') as file:
        file.writelines(txt_lines)

    # Format and save the created XML file
    xml_str = ET.tostring(xml_root, encoding='utf-8')
    formatted_xml = xml.dom.minidom.parseString(xml_str).toprettyxml(indent="   ")

    with open(xml_file_path, 'w', encoding='utf-8') as file:
        file.write('<?xml version="1.0" encoding="utf-8"?>\n')  # Manually write the XML declaration
        file.write(formatted_xml)

# Example usage
txt_file_path = r'Your\Text\File\Path\Here'
xml_file_path = r'Your\Localization\XML\File\Path\Here'
process_txt_and_create_xml(txt_file_path, xml_file_path)