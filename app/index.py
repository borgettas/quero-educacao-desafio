import json
import pandas as pd
import requests


DATA_URL = "https://s3.amazonaws.com/gupy5/production/companies/41683/emails/1679437007669/8408fe80-c80f-11ed-80da-7d3cd1fee4b4/log.txt"


def request_get_data(url: str):

    response = requests.get(DATA_URL)
    
    if response.status_code == 200:
        data = response.text
        
        return data
    else:
        print(f"❌ Request Error - {response.status_code}")


def list_str_dict_to_list_dict(data: str) -> list:

    list_dict = []

    splited_data = data.split("\n")
    
    for item in splited_data:
        if item != '':
            json_object = json.loads(item.replace("'", "\""))
            list_dict.append(json_object)
    
    return list_dict


def main():
    data = request_get_data(DATA_URL)
    splited_data = list_str_dict_to_list_dict(data=data)


if  __name__ == "__main__":
    main()
