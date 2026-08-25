from pathlib import Path

from minecraft_modrinth.utils import input, api_things

# variable to get the directory where we are running the `main.py` file
MODULE_DIR = Path(__file__).resolve().parent

# therefore create a variable for the `minecraft_mods` text file
# INFO: need to convert 'Path' object into a string to be able to use it
MODS_FILE = str(MODULE_DIR / "minecraft_mods.txt")
JSON_FILE = str(MODULE_DIR / "api_response.json")

# variables related to Modrinth
API_URL: str = "https://api.modrinth.com/v2"
WEBSITE_URL: str = "https://modrinth.com"
STAGING_API_URL: str = "https://staging-api.modrinth.com/"
MOD_URL: str = "https://api.modrinth.com/v2/project/sodium/version"


# our main function for the whole 'minecraft_modrinth' project
def main() -> None:
    # mods = input.read_mods_file(MODS_FILE)
    #
    # print(f"Mods in file: {mods}")

    # api_things.test_api_url(STAGING_API_URL)
    # api_things.test_api_url(MOD_URL)
    # api_things.test_api_url(MOD_URL)
    # api_things.test_api_url(TEST)

    api_things.get_cdn_url(API_URL, "sodium", "fabric", "1.21.1", JSON_FILE)
