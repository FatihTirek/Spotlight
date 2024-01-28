import re
import os
import shutil
from pathlib import Path

SPOTLIGHT_PATH = "Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"

assets_path = os.path.join(os.getenv("LOCALAPPDATA"), SPOTLIGHT_PATH)
pictures_path = Path.home() / "Pictures/Saved Pictures"


def main(name='picture', rename=False):
    Path(pictures_path).mkdir(exist_ok=True)

    for file in os.listdir(assets_path):
        file_path = os.path.join(assets_path, file)
        file_size = os.path.getsize(file_path) / 1024

        if file_size > 400:
            new_path = os.path.join(pictures_path, file)
            image_path = Path(new_path).with_suffix(".jpg")

            if not image_path.exists():
                shutil.copy(file_path, pictures_path)
                os.rename(new_path, image_path)

    if rename:
        rename_all(name)


def rename_all(name):
    files = os.listdir(pictures_path)
    number = max(map(get_number, files)) + 1

    for file in files:
        file_path = os.path.join(pictures_path, file)
        renamed_path = Path(file_path).with_stem(f'{name}_{number}')

        os.rename(file_path, renamed_path)
        number += 1


def get_number(text):
    match = re.search(r"picture_([0-9]+)", text, re.IGNORECASE)

    if match is not None:
        return int(match.group(1))

    return 1

if __name__ == "__main__":
    main(rename=False)
