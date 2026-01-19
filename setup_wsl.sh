#!/bin/bash
# WSL2 Setup Script for ETL Learning Project
# Run this script in your WSL2 Ubuntu terminal

echo "======================================"
echo "ETL Learning Project - WSL2 Setup"
echo "======================================"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if we're in WSL
if ! grep -qi microsoft /proc/version; then
    echo "⚠️  This script should be run in WSL2, not Windows!"
    exit 1
fi

echo -e "${YELLOW}Step 1: Installing Python venv package...${NC}"
sudo apt update
sudo apt install -y python3.12-venv python3-pip

echo -e "\n${YELLOW}Step 2: Setting up project in WSL2...${NC}"
cd ~

# Check if project already exists
if [ -d "etl-learning-project" ]; then
    echo "Project already exists in ~/etl-learning-project"
    cd etl-learning-project
else
    echo "Copying project from Windows..."
    cp -r /mnt/c/Users/jonye/Documents/Books/python/etl-learning-project .
    cd etl-learning-project
fi

echo -e "\n${YELLOW}Step 3: Creating Python virtual environment...${NC}"
# Remove old venv if it exists
if [ -d "venv" ]; then
    rm -rf venv
fi

python3 -m venv venv

echo -e "\n${YELLOW}Step 4: Activating virtual environment...${NC}"
source venv/bin/activate

echo -e "\n${YELLOW}Step 5: Installing Python packages...${NC}"
pip install --upgrade pip
pip install pandas requests sqlalchemy python-dotenv openpyxl

echo -e "\n${GREEN}✅ Setup Complete!${NC}"
echo ""
echo "======================================"
echo "Quick Start Commands:"
echo "======================================"
echo ""
echo "1. Navigate to project:"
echo "   cd ~/etl-learning-project"
echo ""
echo "2. Activate virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "3. Run your first pipeline:"
echo "   cd pipelines"
echo "   python simple_etl_template.py"
echo ""
echo "4. Open in VS Code (if installed):"
echo "   code ~/etl-learning-project"
echo ""
echo "======================================"
echo "GitHub Repository:"
echo "https://github.com/jonyeanu123/etl-learning-project"
echo "======================================"
