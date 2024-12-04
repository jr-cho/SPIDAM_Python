import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent / "src"))

from src.gui import create_gui  

if __name__ == "__main__":
    create_gui()