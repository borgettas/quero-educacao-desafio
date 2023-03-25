import json
import pandas as pd
import requests
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


DATA_URL = "https://s3.amazonaws.com/gupy5/production/companies/41683/emails/1679437007669/8408fe80-c80f-11ed-80da-7d3cd1fee4b4/log.txt"


def request_get_data(url: str):

    response = requests.get(DATA_URL)
    
    if response.status_code == 200:
        data = response.text
        
        return data
    else:
        print(f"❌ Request Error - {response.status_code}")


def str_dict_to_list_dict(data: str) -> list:

    list_dict = []

    splited_data = data.split("\n")
    
    for item in splited_data:
        if item != '':
            json_object = json.loads(item.replace("'", "\""))
            list_dict.append(json_object)
    
    return list_dict


def list_dict_to_dataframe(data: list) -> pd.DataFrame:
	
    df = pd.DataFrame.from_records(data)
    
    return df


def transform_type_columns(df: pd.DataFrame) -> pd.DataFrame:
    
    df["statusCode"] = df["statusCode"].astype(int)

    return df


def generate_summary_erros_success(df: pd.DataFrame) -> str:

    df["statusCode_success"] = df.apply(lambda row: 1 if row.statusCode >= 200 and row.statusCode <= 399 else 0, axis = 1)
    df["statusCode_error"] = df.apply(lambda row: 1 if row.statusCode >= 400 and row.statusCode <= 599 else 0, axis = 1)


    df_summary = df.groupby("path")["statusCode_error", "statusCode_success"].agg('sum').reset_index()

    df_summary["errorCount"] = df_summary.apply(lambda row: round((row.statusCode_error / (row.statusCode_error + row.statusCode_success) * 100), 2), axis = 1)
    df_summary["successCount"] = df_summary.apply(lambda row: round((row.statusCode_success / (row.statusCode_error + row.statusCode_success) * 100), 2), axis = 1)

    list_dict = json.dumps(df_summary[["path",  "errorCount", "successCount"]].to_dict(orient = 'records'), indent=2)

    return list_dict


def main():
    data = request_get_data(DATA_URL)
    splited_data = str_dict_to_list_dict(data=data)
    df = list_dict_to_dataframe(data=splited_data)
    df = transform_type_columns(df=df)
    summary = generate_summary_erros_success(df=df)

    print(
        summary
    ) 


if  __name__ == "__main__":
    main()
