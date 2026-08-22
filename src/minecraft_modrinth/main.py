from os import getcwd

from minecraft_modrinth.utils import input


# our main function for the whole 'minecraft_modrinth' project
def main() -> None:
    # mods = input.read_mods_file("minecraft_mods.txt")
    mods = input.read_mods_file(getcwd() + "/src/minecraft_modrinth/minecraft_mods.txt")

    print(f"Mods in file: {mods}")
