from pathlib import Path

from minecraft_modrinth.utils import input

# variable to get the directory where we are running the `main.py` file
MODULE_DIR = Path(__file__).resolve().parent

# therefore create a variable for the `minecraft_mods` text file
# INFO: need to convert 'Path' object into a string to be able to use it
MODS_FILE = str(MODULE_DIR / "minecraft_mods.txt")


# our main function for the whole 'minecraft_modrinth' project
def main() -> None:
    mods = input.read_mods_file(MODS_FILE)

    print(f"Mods in file: {mods}")
