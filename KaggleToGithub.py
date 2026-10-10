import kagglehub
import shutil
from pathlib import Path

# Current project folder (where this script is located)
current_folder = Path(__file__).resolve().parent

# Download dataset from Kaggle
download_path = Path(
    kagglehub.dataset_download("ukveteran/adventure-works")
)

# Copy dataset files into the current project folder
for item in download_path.iterdir():
    destination = current_folder / item.name

    if item.is_dir():
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(item, destination)
    else:
        shutil.copy2(item, destination)

print("Dataset files saved to:", current_folder)