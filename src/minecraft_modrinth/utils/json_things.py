# helper functions / utilities related to the JSON data "manipulation"

# import the 'json' Python module
import json


# convert any vanilla Python dictionary to have 'JSON' formatting
def convert_dict_to_json(json_response: dict):
    # iterate through the key, value pairs of the Python dictionary
    for key, value in json_response.items():
        # try to "decode" the string values that might contains 'JSON' data
        try:
            # check if the current value is a string
            if isinstance(value, str):
                # meaning that the data can be loaded a 'JSON'
                json_response[key] = json.loads(value)

        # if the current value could not be converted
        except json.JSONDecodeError, TypeError:
            # do basically nothing with that data
            pass

    # finally display the Python dictionary with a proper 'JSON' formatting
    print("\n" + json.dumps(json_response, indent=2))


# write the JSON output to a file
def write_json_output(json_data, file: str):
    # write the data to the appropriate JSON file
    with open(file, "w") as api_response_file:
        api_response_file.write(json.dumps(json_data, indent=2))


# read the JSON data and extract the CDN URL
def read_json_get_cdn_url(file):
    # open the file for reading
    with open(file, "r") as api_response_file:
        # read the whole file all at once
        # NOTE: even though not recommended to read the whole file at once
        # I think I will have to do this so that we get the full "picture" / contents
        data = api_response_file.read()

        data = data.replace("\t", "")
        data = data.replace("\n", "")
        data = data.replace(",}", "}")
        data = data.replace(",]", "]")

        # make that 'JSON' data into actual 'JSON' data for Python to understand
        actual_json_data = json.loads(data)

        # check if the data contains empty list ==> error found
        if len(actual_json_data) == 0:
            print("Empty ==> Error in Either Modname / Mod-loader / Game Version")

        else:
            count = 0

            for i in range(len(actual_json_data)):
                version_type = actual_json_data[i]["version_type"]

                if version_type == "release":
                    count = i
                    break

            # get the CDN URL
            # ==> it's actually so fucking easy when you use the correct API URL :)
            fileurl = actual_json_data[count]["files"][0]["url"]

            # simply display the URL
            print(fileurl)

            print()
            name = fileurl.split("/")[-1].replace("%", "-")

            print(name)
