# Quick Start Guide for Jupyter

## Starting Jupyter in WSL2

### Option 1: JupyterLab (Modern UI - Recommended)

```bash
# 1. Open WSL2
wsl

# 2. Navigate to project
cd ~/etl-learning-project

# 3. Activate virtual environment
source venv/bin/activate

# 4. Start JupyterLab
jupyter lab
```

A browser will open automatically with JupyterLab!

---

### Option 2: Classic Jupyter Notebook

```bash
# 1-3. Same as above

# 4. Start Jupyter Notebook
jupyter notebook
```

---

### Option 3: VS Code (Best for Development)

```bash
# 1. Open project in VS Code from WSL
cd ~/etl-learning-project
code .

# 2. In VS Code:
#    - Open any .ipynb file
#    - Click "Select Kernel" (top-right)
#    - Choose: Python 3.11.x ('venv': venv)
#    - Press Shift+Enter to run cells
```

---

## Quick Commands

### Check What's Running
```bash
jupyter notebook list
```

### Stop Jupyter
Press `Ctrl+C` twice in the terminal where Jupyter is running

---

## First Time Setup

If you get "kernel not found" error:

```bash
cd ~/etl-learning-project
source venv/bin/activate
python -m ipykernel install --user --name=etl-venv --display-name="ETL Python (venv)"
```

---

## What to Try First

1. Open `notebooks/01_getting_started.ipynb`
2. Run all cells (Cell → Run All)
3. Modify the code and experiment
4. Try the practice exercises at the bottom

---

## Installed Packages

You now have:
- ✅ jupyter
- ✅ jupyterlab
- ✅ ipykernel
- ✅ ipywidgets
- ✅ notebook
- ✅ pandas
- ✅ requests
- ✅ sqlalchemy
- ✅ python-dotenv

---

## Tips

1. **Always activate venv first!**
   ```bash
   source venv/bin/activate
   ```

2. **Jupyter runs on port 8888 by default**
   - URL: http://localhost:8888

3. **Save notebooks frequently**
   - Use Ctrl+S or File → Save

4. **Restart kernel if things get weird**
   - Kernel → Restart & Clear Output

---

## Troubleshooting

### Port Already in Use
```bash
jupyter lab --port 8889
```

### Module Not Found
Make sure venv is activated and kernel is selected correctly

### Browser Doesn't Open
Copy the URL from terminal (looks like: http://localhost:8888/?token=...)

---

Happy Learning! 🚀
