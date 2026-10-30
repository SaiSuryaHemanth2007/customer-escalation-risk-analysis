
from pathlib import Path
import nbformat as nbf

notebooks = {
    "01_data_understanding.ipynb": [
        "# 01 - Data Understanding",
        "Inspect dataset dimensions, columns, data types and sample records."
    ],
    "02_data_cleaning.ipynb": [
        "# 02 - Data Cleaning",
        "Inspect missing values, duplicates and data inconsistencies."
    ],
    "03_kpi_analysis.ipynb": [
        "# 03 - KPI Analysis",
        "Define and calculate KPIs using the official dataset definitions."
    ],
    "04_escalation_eda.ipynb": [
        "# 04 - Escalation EDA",
        "Explore escalation patterns and the eight official challenge tasks."
    ]
}

folder = Path("notebooks")
folder.mkdir(exist_ok=True)

for filename, content in notebooks.items():
    notebook = nbf.v4.new_notebook()

    notebook.cells = [
        nbf.v4.new_markdown_cell(content[0]),
        nbf.v4.new_markdown_cell(content[1]),
        nbf.v4.new_code_cell("# Dataset analysis will be added after the dataset is released.")
    ]

    path = folder / filename
    nbf.write(notebook, path)

    print(f"Created valid notebook: {path}")

print("\nAll four notebooks are ready!")
