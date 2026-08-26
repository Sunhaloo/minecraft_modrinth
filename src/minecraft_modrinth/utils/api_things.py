# helper functions / utilities related to the APIs

# import the "downloaded" 'requests' module
import requests

# import the functions found inside the `json_things.py` file
from . import json_things
from pathlib import Path

DOWNLOAD_LOCATION: str = str(Path("~/Downloads").expanduser())


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


# try to download the JAR file from the URL by writing to a file
def download_jar_file(cdn_url: str, filename: str, write_location: str):
    cdn_api_response = requests.models.Response = requests.get(cdn_url)

    if cdn_api_response.ok:
        with open(f"{DOWNLOAD_LOCATION}/{filename}", "wb") as mod_file:
            mod_file.write(cdn_api_response.content)


# try to get the CDN URL from the API URL
def get_cdn_url(
    API_URL: str, modname: str, modloader: str, game_version, api_response_file_name
):
    # create the parameter Python dictionary
    params = {"loaders": f'["{modloader}"]', "game_versions": f'["{game_version}"]'}

    # build the full API URL so that we can try to get a response from
    full_api_url = f"{API_URL}/project/{modname}/version"

    # try to get an API response from the `full_api_url` URL
    api_response = requests.models.Response = requests.get(full_api_url, params=params)

    # if we do get something back from the API URL
    if api_response.ok:
        # call the function to write the data to an appropriate file
        json_things.write_json_output(api_response.json(), api_response_file_name)

        # call the function to display the CDN URL
        fileurl, filename = json_things.read_json_get_cdn_url(api_response_file_name)

        # call the function to download the JAR file in question
        download_jar_file(fileurl, filename, DOWNLOAD_LOCATION)
