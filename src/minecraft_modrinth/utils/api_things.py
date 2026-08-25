# helper functions / utilities related to the APIs

# import the "downloaded" 'requests' module
import requests

# import the functions found inside the `json_things.py` file
from . import json_things


# test the API URL as per the documentation
def test_api_url(API_URL: str):
    # try to get an API response from the `API_URL`
    api_response: requests.models.Response = requests.get(API_URL)

    # if we do get something back from the API URL
    if api_response.ok:
        try:
            # display the Python dictionary with proper 'JSON' formatting
            json_things.convert_dict_to_json(api_response.json())

        except AttributeError:
            print(api_response.json())

        return api_response.json()

    else:
        print(f"\n--> Status Code: {api_response.status_code} <--\n")


# try to get the CDN URL from the API URL
def get_cdn_url(
    API_URL: str, modname: str, modloader: str, game_version, api_response_file_name
):
    # create the parameter Python dictionary
    params = {"loaders": f'["{modloader}"]', "game_versions": f'["{game_version}"]'}

    # build the full API URL so that we can try to get a response from
    full_api_url = f"{API_URL}/project/{modname}"

    # try to get an API response from the `full_api_url` URL
    api_response = requests.models.Response = requests.get(full_api_url, params=params)

    # if we do get something back from the API URL
    if api_response.ok:
        print(api_response.json())

        # call the function to write the data to an appropriate file
        json_things.write_json_output(api_response.json(), api_response_file_name)
