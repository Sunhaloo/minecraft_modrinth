# helper functions / utilities related to the APIs

# import the "downloaded" 'requests' module
import requests

# import the functions found inside the `json_things.py` file
from . import json_things


# test the staging API URL as per the documentation
def test_api_url(API_URL: str):
    # try to get an API response from the `API_URL`
    api_response: requests.models.Response = requests.get(API_URL)

    # if we do get something back from the API URL
    if api_response.ok:
        # display the Python dictionary with proper 'JSON' formatting
        json_things.convert_dict_to_json(api_response.json())

    else:
        print(f"\n--> Status Code: {api_response.status_code} <--\n")
