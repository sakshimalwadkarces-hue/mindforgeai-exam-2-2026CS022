from pathlib import Path
import shutil
import pandas as pd

project_dir = Path(__file__).resolve().parent
workspace_root = project_dir.parent.parent
source_file = workspace_root / "Section_C" / "Practical_Notebook" / "week_assesment.csv"
destination_file = project_dir / "data" / "week_assesment.csv"

destination_file.parent.mkdir(parents=True, exist_ok=True)
shutil.copy2(source_file, destination_file)

print(f"Copied: {source_file} -> {destination_file}")

df = pd.read_csv(destination_file)
print("\nFirst 5 rows of the copied CSV:\n")
print(df.head())
