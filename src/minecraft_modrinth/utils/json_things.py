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
        except (json.JSONDecodeError, TypeError):
            # do basically nothing with that data
            pass

    # finally display the Python dictionary with a proper 'JSON' formatting
    print("\n" + json.dumps(json_response, indent=2))
