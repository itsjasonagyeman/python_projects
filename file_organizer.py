import os
import shutil

source_folder = r"C:\Users\Admin\Desktop\Stats"

categories = {
    'Text' : ['.txt'],
    'Pdf' : ['.pdf']
}

for filename in os.listdir(source_folder):
    filepath = os.path.join(source_folder, filename)

    if os.path.isfile(filepath):
        ext = os.path.splitext(filename)[1].lower()

        moved = False
        for folder, extensions in categories.items():
            if ext in extensions:
                target_folder = os.path.join(source_folder, folder)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(filepath, os.path.join(target_folder, filename))
                moved = True
                break

        # Optional: Move unknown files to "Others"
        if not moved:
            other_folder = os.path.join(source_folder, 'Others')
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(filepath, os.path.join(other_folder, filename))