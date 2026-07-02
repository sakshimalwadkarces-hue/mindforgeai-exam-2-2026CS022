from pathlib import Path
import shutil

project_dir = Path(__file__).resolve().parent
workspace_root = project_dir.parent.parent
source_file = workspace_root / "Section_C" / "Practical_Notebook" / "Section_C_Notebook.ipynb"
destination_file = project_dir / "notebooks" / "Section_C_Notebook.ipynb"

destination_file.parent.mkdir(parents=True, exist_ok=True)
shutil.copy2(source_file, destination_file)

if destination_file.exists():
    size = destination_file.stat().st_size
    print(f"✅ Notebook successfully copied and verified!")
    print(f"Destination: {destination_file}")
    print(f"File size: {size} bytes")
else:
    raise FileNotFoundError(f"Copy failed: {destination_file} was not created")
