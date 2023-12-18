from PIL import Image
import os

def create_image_atlas(images_directory, atlas_path, atlas_size=(2048, 2048)):
    atlas = Image.new('RGBA', atlas_size)
    x, y = 0, 0

    prefix_to_background = {
        'Arcane': 'action_bg2.dds', 'Fire': 'action_bg2.dds', 'Life': 'action_bg2.dds',
        'Lightning': 'action_bg2.dds', 'Nature': 'action_bg2.dds', 'Psychic': 'action_bg2.dds',
        'Water': 'action_bg2.dds', 'Wind': 'action_bg2.dds',
        'Blood': 'action_bg2.dds', 'Chaos': 'action_bg2.dds', 'Cold': 'action_bg2.dds',
        'Earth': 'action_bg2.dds', 'Reality': 'action_bg2.dds',
        'Force': 'action_bg2.dds', 'Time': 'action_bg2.dds',
        'Darkness': 'action_bg2.dds', 'Thunder': 'action_bg2.dds',
        'Gravity': 'action_bg2.dds', 'Necrotic': 'action_bg2.dds', 'Shadow': 'action_bg2.dds'
    }

    for image_file in sorted(os.listdir(images_directory)):
        if image_file.endswith('.png'):
            prefix = image_file.split('_')[0]
            background_name = prefix_to_background.get(prefix)
            if background_name:
                background = Image.open(os.path.join(images_directory, background_name))
                overlay_image = Image.open(os.path.join(images_directory, image_file))
                bg_width, bg_height = background.size
                overlay_width, overlay_height = overlay_image.size
                overlay_x = (bg_width - overlay_width) // 2
                overlay_y = (bg_height - overlay_height) // 2
                background.paste(overlay_image, (overlay_x, overlay_y), overlay_image)

                # Place the combined image onto the atlas
                atlas.paste(background, (x, y))
                x += overlay_width
                if x >= atlas_size[0]:
                    x = 0
                    y += overlay_height

    # Save the final atlas
    atlas.save(atlas_path)

# Example usage
images_directory = 'path\\to\\your\\64x64\\icons'
atlas_path = 'path\\to\\your\\atlas_icons.dds'
create_image_atlas(images_directory, atlas_path)