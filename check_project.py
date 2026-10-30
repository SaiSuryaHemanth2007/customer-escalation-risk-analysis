
from pathlib import Path
import importlib.util
import subprocess
import json

ROOT = Path(__file__).resolve().parent

print("\n" + "=" * 60)
print(" CUSTOMER ESCALATION RISK - PROJECT HEALTH CHECK")
print("=" * 60)

passed = 0
failed = 0
warnings = 0


def check(name, condition, warning=False):
    global passed, failed, warnings

    if condition:
        print(f"[PASS] {name}")
        passed += 1
    elif warning:
        print(f"[WARN] {name}")
        warnings += 1
    else:
        print(f"[FAIL] {name}")
        failed += 1


# 1. Documentation
print("\n1. DOCUMENTATION")

documents = [
    "README.md",
    "docs/HLD.md",
    "docs/LLD.md",
    "docs/architecture.md",
    "docs/data_flow.md",
    "docs/module_design.md",
    "docs/technology_stack.md",
    "docs/testing_strategy.md",
]

for file in documents:
    path = ROOT / file
    check(file, path.is_file() and path.stat().st_size > 0)


# 2. Source code
print("\n2. SOURCE CODE")

source_files = [
    "src/__init__.py",
    "src/ingestion/__init__.py",
    "src/ingestion/data_loader.py",
    "src/validation/__init__.py",
    "src/validation/data_validator.py",
    "src/processing/__init__.py",
    "src/processing/data_cleaner.py",
    "src/analytics/__init__.py",
    "src/analytics/kpi_calculations.py",
    "src/analytics/escalation_analysis.py",
    "src/visualization/__init__.py",
    "src/visualization/visualizations.py",
    "dashboard/app.py",
]

for file in source_files:
    path = ROOT / file
    check(file, path.is_file())


# 3. Jupyter notebooks
print("\n3. JUPYTER NOTEBOOKS")

notebooks = [
    "notebooks/01_data_understanding.ipynb",
    "notebooks/02_data_cleaning.ipynb",
    "notebooks/03_kpi_analysis.ipynb",
    "notebooks/04_escalation_eda.ipynb",
]

for file in notebooks:
    path = ROOT / file
    valid = False

    if path.is_file() and path.stat().st_size > 0:
        try:
            with open(path, encoding="utf-8") as f:
                notebook = json.load(f)

            valid = (
                notebook.get("nbformat") == 4
                and isinstance(notebook.get("cells"), list)
            )
        except (json.JSONDecodeError, OSError):
            valid = False

    check(file, valid)


# 4. Python libraries
print("\n4. PYTHON LIBRARIES")

libraries = [
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "openpyxl",
    "pytest",
    "plotly",
    "notebook",
    "streamlit",
]

for library in libraries:
    installed = importlib.util.find_spec(library) is not None
    check(
        library,
        installed,
        warning=(library == "streamlit")
    )


# 5. Project configuration
print("\n5. PROJECT CONFIGURATION")

check(
    ".gitignore",
    (ROOT / ".gitignore").is_file()
)

check(
    "requirements.txt",
    (ROOT / "requirements.txt").is_file()
)

check(
    "Virtual environment",
    (ROOT / ".venv" / "Scripts" / "python.exe").is_file()
)


# 6. Dataset folders
print("\n6. DATASET FOLDERS")

for folder in ["data/raw", "data/processed"]:
    check(folder, (ROOT / folder).is_dir())

print("\nDataset inspection:")
raw_folder = ROOT / "data/raw"

if raw_folder.is_dir():
    datasets = list(raw_folder.glob("*.csv"))
    datasets += list(raw_folder.glob("*.xlsx"))
    datasets += list(raw_folder.glob("*.xls"))

    if datasets:
        print(f"[INFO] Found {len(datasets)} dataset file(s).")
    else:
        print("[INFO] No dataset found yet. Expected before hackathon.")


# 7. Git
print("\n7. GIT STATUS")

try:
    result = subprocess.run(
        ["git", "status", "--short"],
        cwd=ROOT,
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        check("Git repository", True)

        if result.stdout.strip():
            print("[INFO] Files need committing:")
            print(result.stdout)
        else:
            print("[INFO] Working tree is clean.")
    else:
        check("Git repository", False)

except FileNotFoundError:
    check("Git installed", False)


# Final report
print("\n" + "=" * 60)
print(" FINAL PROJECT HEALTH REPORT")
print("=" * 60)

print(f"Passed   : {passed}")
print(f"Failed   : {failed}")
print(f"Warnings : {warnings}")

if failed == 0 and warnings == 0:
    print("\nEXCELLENT! All checks passed.")
elif failed == 0:
    print("\nGOOD! Some optional items still need attention.")
else:
    print("\nACTION REQUIRED: Fix failed checks before proceeding.")

print("=" * 60)
