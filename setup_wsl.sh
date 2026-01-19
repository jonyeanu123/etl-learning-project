#!/bin/bash
# WSL2 Setup Script for ETL Learning Project
# Run this script in your WSL2 Ubuntu terminal

echo "======================================"
echo "ETL Learning Project - WSL2 Setup"
echo "======================================"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if we're in WSL
if ! grep -qi microsoft /proc/version; then
    echo -e "${RED}⚠️  This script should be run in WSL2, not Windows!${NC}"
    echo "Please run: wsl"
    exit 1
fi

echo -e "${YELLOW}Step 1: Installing Python venv package...${NC}"
sudo apt update
sudo apt install -y python3.12-venv python3-pip

echo -e "\n${YELLOW}Step 2: Setting up project in WSL2...${NC}"
cd ~

# Check if project already exists
if [ -d "etl-learning-project" ]; then
    echo "Project directory exists, cleaning up old venv..."
    cd etl-learning-project
    rm -rf venv
else
    echo "Creating project from Windows files..."
    mkdir -p etl-learning-project
    cd etl-learning-project

    # Copy only the necessary files (exclude venv)
    cp /mnt/c/Users/jonye/Documents/Books/python/etl-learning-project/.gitignore . 2>/dev/null || true
    cp /mnt/c/Users/jonye/Documents/Books/python/etl-learning-project/*.md . 2>/dev/null || true
    cp /mnt/c/Users/jonye/Documents/Books/python/etl-learning-project/*.txt . 2>/dev/null || true
    cp /mnt/c/Users/jonye/Documents/Books/python/etl-learning-project/*.sh . 2>/dev/null || true
    cp -r /mnt/c/Users/jonye/Documents/Books/python/etl-learning-project/.git . 2>/dev/null || true
    cp -r /mnt/c/Users/jonye/Documents/Books/python/etl-learning-project/data . 2>/dev/null || true
    cp -r /mnt/c/Users/jonye/Documents/Books/python/etl-learning-project/pipelines . 2>/dev/null || true
    cp -r /mnt/c/Users/jonye/Documents/Books/python/etl-learning-project/utils . 2>/dev/null || true
    cp -r /mnt/c/Users/jonye/Documents/Books/python/etl-learning-project/notebooks . 2>/dev/null || true
    cp -r /mnt/c/Users/jonye/Documents/Books/python/etl-learning-project/logs . 2>/dev/null || true
fi

echo -e "\n${YELLOW}Step 3: Creating Python virtual environment...${NC}"
python3 -m venv venv

echo -e "\n${YELLOW}Step 4: Activating virtual environment...${NC}"
source venv/bin/activate

echo -e "\n${YELLOW}Step 5: Installing Python packages...${NC}"
pip install --upgrade pip
pip install pandas requests sqlalchemy python-dotenv openpyxl

echo -e "\n${GREEN}✅ Setup Complete!${NC}"
echo ""
echo "======================================"
echo "Project Location: ~/etl-learning-project"
echo "======================================"
echo ""
echo "Quick Start Commands:"
echo "======================================"
echo ""
echo "1. Navigate to project:"
echo "   ${YELLOW}cd ~/etl-learning-project${NC}"
echo ""
echo "2. Activate virtual environment:"
echo "   ${YELLOW}source venv/bin/activate${NC}"
echo ""
echo "3. Run your first pipeline:"
echo "   ${YELLOW}cd pipelines${NC}"
echo "   ${YELLOW}python simple_etl_template.py${NC}"
echo ""
echo "4. Open in VS Code (if installed):"
echo "   ${YELLOW}code ~/etl-learning-project${NC}"
echo ""
echo "======================================"
echo "GitHub Repository:"
echo "https://github.com/jonyeanu123/etl-learning-project"
echo "======================================"
echo ""
echo -e "${GREEN}You're all set! Start learning! 🚀${NC}"
