import os
import sys
import shutil

xml_content = """<?xml version="1.0" encoding="utf-8"?>
<save>
<version major="1" minor="0" revision="0" build="0" lslib_meta="v1,bswap_guids" />
	<region id="Dependencies">
		<node id="Dependencies">
			<children>
                <!-- Your Dependencies Here -->				
			</children>
		</node>
	</region>
    <region id="Effect">
		<node id="Effect">
			<attribute id="Duration" type="float" value="3" />
			<children>
				<node id="EffectComponents">
					<children>
                        <!-- Your EffectComponents Here -->
                    </children>
                </node>
                <node id="Input">
                    <children>
                        <!-- Your Inputs Here -->
                    </children>
                </node>
                <node id="Phases">
                    <children>
                        <!-- Your Phases Here -->
                    </children>
                </node>
            </children>
        </node>
    </region>
</save>
"""

def backup_file(file_path, backup_directory):
    os.makedirs(backup_directory, exist_ok=True)
    
    filename = os.path.basename(file_path)
    backup_path = os.path.join(backup_directory, filename)
    shutil.copyfile(file_path, backup_path)
    print(f"Backup created: {backup_path}")
    return backup_path

def mt_lsfx_filler(root_directory, backup_directory):
    backup_paths = []
    try:
        # Creating backups and modifying empty files
        for root, dirs, files in os.walk(root_directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    if os.path.getsize(file_path) == 0:  # Check if file is empty
                        backup_path = backup_file(file_path, backup_directory)
                        backup_paths.append(backup_path)
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(xml_content)
                            print(f"XML added to: {file_path}")
                    else:
                        print(f"Skipped non-empty file: {file_path}")
                except Exception as e:
                    print(f"An error occurred: {e}")

    except Exception as e:
        print(f"Error occurred while making changes: {e}")
        # Revert changes in case of an error
        for path in backup_paths:
            if os.path.exists(path):
                original_path = os.path.join(root_directory, os.path.basename(path))
                shutil.copyfile(path, original_path)
                print(f"Reverted changes for: {original_path}")
            else:
                print(f"Backup not found for: {path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mt_lsfx_filler.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        backup_dir = r"your\\file\\path\\here"  # Change this to your backup directory path
        mt_lsfx_filler(directory_path, backup_dir)
