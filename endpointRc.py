# This script validates the Endpoints response code.
# Code will responsed with the Response Code of 200 and errors 404 if the endpoint is invalid.

import json
import requests

endpoint_json = 'endpoint.json'
endpoint_error = 'endpoint_error.json' 

def make_request(url, auth):
    try:
        response = requests.get(url)
        return response
    except requests.exceptions.RequestException as e:
        print(f"HTTP request error: {e}")
        return None
    
def gather_url(url_json):
    try:
        with open(url_json, 'r') as file:
            data = json.load(file)

            if "Endpoints" in data:
                endpoints = data["Endpoints"]

                for url_name, details in endpoints.items():
                    url = details.get('url')
                    auth = details.get('auth')
                    print(f"\nDetail of endpoints: {url_name}")
                    print(f"URL: {url}")

                    if url:
                        response = make_request(url, auth)
                        if response:
                            print(f"Response code: {response.status_code}")
                        else:
                            print(f"Unexpected status code: {response.status_code}")
            else:
                print("Error: End point not found on the json")
    except FileNotFoundError:
        print(f"File Not found {url_json}")
    except json.JSONDecodeError as e:
        print(f"Decoding json error: {e}")



if __name__ == "__main__":
    gather_url(endpoint_json)
    #gather_url(endpoint_error)
