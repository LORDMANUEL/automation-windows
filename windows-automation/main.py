import sys
import os

# Set the working directory to the directory containing this script
# This makes relative paths for data files work correctly
project_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(project_dir)

# Add the src directory to the Python path
sys.path.append('src')

from ui.cli import main_loop

if __name__ == "__main__":
    main_loop()
