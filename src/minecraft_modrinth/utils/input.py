# helper functions / utilities related to the input of data in the program


# read the mods written in the text file and popuplate list
def read_mods_file(file_path: str) -> list[str]:
    mods_list: list[str] = []

    try:
        # read each Minecraft mods written inside the file and populate list
        with open(file_path, "r") as mods_file:
            for line in mods_file:
                # remove all the unncessary "baggage" with the line
                stripped_line = line.strip()

                # check if the line contains Minecraft mods name or is a comment
                if not stripped_line or stripped_line.startswith("#"):
                    continue

                else:
                    # add the required Minecraft mods to the list
                    mods_list.append(stripped_line.lower())

    except FileNotFoundError as e:
        print(e)

    return mods_list
