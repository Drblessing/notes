# Install .benv for bin scripts
# Run from ~/Github/notes

# Navigate to bin
cd bin 

# Install python
python3 -m venv .benv

# Activate the virtual environment
source .benv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt
