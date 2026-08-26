from pathlib import Path

from minecraft_modrinth.utils import input, api_things

# variable to get the directory where we are running the `main.py` file
MODULE_DIR = Path(__file__).resolve().parent

# therefore create a variable for the `minecraft_mods` text file
# INFO: need to convert 'Path' object into a string to be able to use it
MODS_FILE = str(MODULE_DIR / "minecraft_mods.txt")

# variables related to Modrinth
API_URL: str = "https://api.modrinth.com/v2"


# our main function for the whole 'minecraft_modrinth' project
def main() -> None:
    # create a file to get the data ==> basically following 'Downrinth'
    json_file = str(MODULE_DIR / "api_response.json")

    # call the function to read the data from the `minecraft_modrinth.txt` file
    mods_list: list[str] = input.read_mods_file(MODS_FILE)

    # iterate through the list of mods
    for i in range(len(mods_list)):
        # download each of the mods found inside that list
        api_things.get_cdn_url(API_URL, mods_list[i], "fabric", "1.21.1", json_file)

    # call the function to get the CDN URL
    # api_things.get_cdn_url(API_URL, "sodium", "fabric", "1.21.1", json_file)
    # api_things.get_cdn_url(API_URL, "entityculling", "fabric", "1.21.1", json_file)
