# WSL2 Development Setup Guide

## Quick Setup (Recommended)

### Option 1: Run the Setup Script

1. **Open WSL2 Terminal** (Ubuntu)
   - In VS Code terminal, type: `wsl`
   - OR open Windows Terminal and select "Ubuntu"

2. **Run the setup script**:
   ```bash
   cd /mnt/c/Users/jonye/Documents/Books/python/etl-learning-project
   chmod +x setup_wsl.sh
   ./setup_wsl.sh
   ```

3. **Follow the prompts** and the script will:
   - Install Python venv package
   - Copy project to `~/etl-learning-project`
   - Create virtual environment
   - Install all required packages

---

## Manual Setup (If Script Doesn't Work)

### Step 1: Install Python venv
```bash
wsl
sudo apt update
sudo apt install -y python3.12-venv python3-pip
```

### Step 2: Copy Project to WSL2
```bash
cd ~
cp -r /mnt/c/Users/jonye/Documents/Books/python/etl-learning-project .
cd etl-learning-project
```

### Step 3: Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install --upgrade pip
pip install pandas requests sqlalchemy python-dotenv openpyxl
```

### Step 5: Test the Setup
```bash
cd pipelines
python simple_etl_template.py
```

---

## Understanding Your Setup

### File Access Patterns

#### **Windows → WSL2**
Access Windows files from WSL2 using `/mnt/`:
```bash
# Windows: C:\Users\jonye\Documents\
# WSL2:    /mnt/c/Users/jonye/Documents/
```

#### **WSL2 → Windows**
Access WSL2 files from Windows using `\\wsl$\`:
```
WSL2:    /home/justin/etl-learning-project/
Windows: \\wsl$\Ubuntu\home\justin\etl-learning-project\
```

---

## Recommended Workflow

### Using WSL2 (Best Performance)

1. **Work from WSL2 home directory**:
   ```bash
   cd ~/etl-learning-project
   source venv/bin/activate
   ```

2. **Edit in VS Code**:
   ```bash
   code ~/etl-learning-project
   ```
   VS Code will automatically detect WSL2 and install the WSL extension

3. **Run Python scripts**:
   ```bash
   cd pipelines
   python simple_etl_template.py
   ```

### Why WSL2 for Development?

✅ **Better performance** - Native Linux filesystem
✅ **Better tools** - Access to Linux tools and utilities
✅ **Better packages** - Easier to install data engineering tools
✅ **Production-like** - Most data engineering runs on Linux
✅ **Docker integration** - Works seamlessly with Docker

---

## Daily Commands

### Starting Work
```bash
# Open WSL2
wsl

# Navigate to project
cd ~/etl-learning-project

# Activate environment
source venv/bin/activate

# Check git status
git status
```

### Running Exercises
```bash
cd ~/etl-learning-project/pipelines
python simple_etl_template.py
python api_etl_example.py
```

### Committing Changes
```bash
cd ~/etl-learning-project
git add .
git commit -m "Completed Exercise 1"
git push
```

---

## VS Code Integration

### Install WSL Extension
1. Open VS Code
2. Install "Remote - WSL" extension
3. Press `F1` → Type "WSL: Connect to WSL"

### Open Project in WSL
```bash
cd ~/etl-learning-project
code .
```

This opens VS Code connected to WSL2 - you get the best of both worlds!

---

## Troubleshooting

### Python Not Found
```bash
# Install Python
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
```

### Permission Issues
```bash
# Make scripts executable
chmod +x setup_wsl.sh
```

### Git Not Configured
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Virtual Environment Not Activating
```bash
# Make sure you're in the project directory
cd ~/etl-learning-project

# Activate
source venv/bin/activate

# You should see (venv) in your prompt
```

---

## Project Locations

### Main Project (WSL2 - Use This!)
```
~/etl-learning-project/
```

### Original (Windows - For Reference)
```
C:\Users\jonye\Documents\Books\python\etl-learning-project\
```

### GitHub
```
https://github.com/jonyeanu123/etl-learning-project
```

---

## Syncing Between Windows and WSL2

### Option A: Work in WSL2 Only (Recommended)
Just work in `~/etl-learning-project` and push to GitHub

### Option B: Keep in Sync
```bash
# Copy WSL2 → Windows
cp -r ~/etl-learning-project/* /mnt/c/Users/jonye/Documents/Books/python/etl-learning-project/

# Copy Windows → WSL2
cp -r /mnt/c/Users/jonye/Documents/Books/python/etl-learning-project/* ~/etl-learning-project/
```

**Better**: Use Git for syncing:
```bash
# In WSL2
cd ~/etl-learning-project
git add .
git commit -m "My changes"
git push

# In Windows
cd C:\Users\jonye\Documents\Books\python\etl-learning-project
git pull
```

---

## Tips for Success

1. **Always activate venv** before running Python scripts
2. **Use WSL2 terminal** for better Linux compatibility
3. **Commit often** to track your learning progress
4. **Keep README open** in your browser for quick reference

---

## Next Steps

1. Run the setup script OR follow manual setup
2. Test by running the first pipeline
3. Start Week 1 of the Learning Plan
4. Complete Exercise 1
5. Commit and push your first changes

Happy Learning! 🚀
