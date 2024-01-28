import os
import shutil
from pathlib import Path

SPOTLIGHT_PATH = os.path.join(os.getenv("LOCALAPPDATA"), "Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets")
PICTURES_PATH = Path.home() / "Pictures/Saved Pictures"
MAX_FILE_SIZE_KB = 400

def main(name='picture', rename=False):
    Path(PICTURES_PATH).mkdir(exist_ok=True)

    for file in os.listdir(SPOTLIGHT_PATH):
        file_path = os.path.join(SPOTLIGHT_PATH, file)
        file_size = os.path.getsize(file_path) / 1024

        if file_size > MAX_FILE_SIZE_KB:
            image_path = os.path.join(PICTURES_PATH, file)
            image_path_with_suffix = Path(image_path).with_suffix(".jpg")

            if not image_path_with_suffix.exists():
                shutil.copy(file_path, PICTURES_PATH)
                os.rename(image_path, image_path_with_suffix)

    if rename:
        number = 0

        for file in os.listdir(PICTURES_PATH):
            number += 1
            file_path = os.path.join(PICTURES_PATH, file)
            file_path_renamed = Path(file_path).with_stem(f'{name}_{number}')
            
            os.rename(file_path, file_path_renamed)

if __name__ == "__main__":
    should_rename = input("Do you want to rename the images? (Y/N): ").strip().upper()
    
    if should_rename == 'Y':
        name = input("Enter the base name for renamed images (Default \"picture\"): ").strip()
        main(name, True)
    else:
        main()
