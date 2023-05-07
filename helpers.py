# Functions that assist the functionality of the Secret Email Sending API
import requests
import json
import re
from constants import EMAIL_REGEX

def get_empty_kwargs(**kwargs):
    """Return keys of empty kwargs."""
    
    return [key for key, value in kwargs.items() if not value]

def is_valid_email(email):
    """Get if an email is valid or not"""
    
    return bool(re.match(EMAIL_REGEX, email))

def get_urls_from_file(url_filename):
    """Return a list of all URLS found in a file."""
    
    urls = []
    
    with open(url_filename) as url_file:
        
        # Loop through all lines in the file
        for line in url_file:
            
            if ":" in line:
            
                _, url = line.split(":")
                url = url.strip()
                urls.append(url)
    
    return urls
            

def send_json_to_url(dict_to_send, url_to_get_json):
    """Send a JSON string to a URL using the POST method"""
    
    # Convert dictionary to JSON data
    json_str = json.dumps(dict_to_send)
    
    # Make it clear you're sending a JSON object
    headers = {
        "Content-Type" : "application/json"
    }
    
    # Send the POST request to the given URL
    res = requests.post(url_to_get_json, data=json_str, headers=headers)
    
    # Return the response
    return res

def read_res_from_url(response):
    """Read response message from sending a JSON to a URL."""
    
    # If statuc code is 200, continue
    if response.status_code == 200:
        
        json_res = response.json()
        
        # return the json response that is in dict form
        return json_res
    
    else:
        return f"HTTP Error: received status code is: {response.status_code}"
    
    