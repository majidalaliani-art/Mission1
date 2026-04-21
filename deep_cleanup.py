import os
import shutil
import glob

paths_to_delete = [
    'db.sqlite3',
    'core/migrations/0*.py',
    'core/migrations/__pycache__',
]

print("Starting deep cleanup...")

for path_pattern in paths_to_delete:
    files = glob.glob(path_pattern)
    for f in files:
        try:
            if os.path.isdir(f):
                shutil.rmtree(f)
                print(f"Deleted directory: {f}")
            else:
                os.remove(f)
                print(f"Deleted file: {f}")
        except Exception as e:
            print(f"Failed to delete {f}: {e}")

print("Cleanup finished.")
