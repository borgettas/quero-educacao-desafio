import json
import pandas as pd
import requests

from urllib.request import urlopen


DATA_URL = "https://s3.amazonaws.com/gupy5/production/companies/41683/emails/1679437007669/8408fe80-c80f-11ed-80da-7d3cd1fee4b4/log.txt"


def request_get_data(url: str):

    response = requests.get(DATA_URL)
    
    if response.status_code == 200:
        data = response.text
        
        return data
    else:
        print(f"❌ Request Error - {response.status_code}")


def main():
    data = request_get_data(DATA_URL)


if  __name__ == "__main__":
    main()
