# Jupyter Notebooks for ETL Learning

This folder contains interactive Jupyter notebooks to complement your ETL learning journey.

## Available Notebooks

### 1. Getting Started (`01_getting_started.ipynb`)
- Basic data loading with pandas
- Data exploration techniques
- Simple data cleaning operations
- Creating derived columns
- Saving cleaned data

### 2. Data Extraction (`02_data_extraction.ipynb`)
- Reading CSV files
- Reading JSON files
- Calling REST APIs
- Querying databases with SQLAlchemy
- Combining data from multiple sources

## How to Use

### Starting Jupyter Lab (Recommended)

```bash
cd ~/etl-learning-project
source venv/bin/activate
jupyter lab
```

This will:
- Start JupyterLab in your browser
- Provide a modern interface with file browser
- Support multiple tabs and terminals

### Starting Jupyter Notebook (Classic)

```bash
cd ~/etl-learning-project
source venv/bin/activate
jupyter notebook
```

### Using VS Code

VS Code has excellent Jupyter support:
1. Open VS Code in WSL: `code ~/etl-learning-project`
2. Install "Jupyter" extension (if not already installed)
3. Open any `.ipynb` file
4. Select kernel: Choose the Python from your venv
5. Run cells with `Shift+Enter`

## Tips for Notebook Development

### 1. Always Activate Your Virtual Environment First
```bash
source venv/bin/activate
```

### 2. Select the Right Kernel
Make sure to select the Python interpreter from your venv:
- In Jupyter: Kernel → Change Kernel → Python 3
- In VS Code: Top-right kernel selector → Select venv Python

### 3. Run Cells in Order
Notebooks are meant to be run sequentially. Use:
- `Shift+Enter`: Run cell and move to next
- `Ctrl+Enter`: Run cell and stay
- `Alt+Enter`: Run cell and insert new below

### 4. Restart Kernel When Needed
If things get confusing:
- Kernel → Restart & Clear Output
- Then run all cells from the top

### 5. Save Frequently
Notebooks auto-save, but use `Ctrl+S` to save manually.

## Creating Your Own Notebooks

Feel free to create new notebooks for:
- Exploring the exercises from `EXERCISES.md`
- Experimenting with your own data
- Documenting your learning journey
- Building mini-projects

### Template for New Notebooks

```python
# Cell 1: Imports
import pandas as pd
import numpy as np
from datetime import datetime

# Cell 2: Load Data
df = pd.read_csv('../data/raw/your_file.csv')

# Cell 3: Explore
df.head()
df.info()

# Cell 4: Transform
# Your transformations here

# Cell 5: Save
df.to_csv('../data/processed/output.csv', index=False)
```

## Notebook Best Practices

1. **Use Markdown Cells**: Document what each section does
2. **Clear Outputs**: Before committing to git, clear sensitive outputs
3. **Keep It Focused**: One notebook per concept/exercise
4. **Test in Order**: Make sure cells run top-to-bottom
5. **Add Comments**: Explain your thought process

## Converting Notebooks to Scripts

Once you've developed something in a notebook, convert to a Python script:

```bash
# Convert notebook to Python script
jupyter nbconvert --to script 01_getting_started.ipynb

# This creates 01_getting_started.py
```

## Troubleshooting

### Kernel Not Found
```bash
# Register your venv as a Jupyter kernel
python -m ipykernel install --user --name=etl-venv --display-name="ETL Python"
```

### Module Not Found
Make sure you:
1. Activated the virtual environment
2. Selected the correct kernel in Jupyter
3. Installed the required packages

### Port Already in Use
If Jupyter won't start:
```bash
# Specify a different port
jupyter lab --port 8889
```

## Next Steps

1. Start with `01_getting_started.ipynb`
2. Work through `02_data_extraction.ipynb`
3. Create notebooks for exercises from `EXERCISES.md`
4. Build your own exploratory notebooks

Happy learning! 🚀
