import argparse
import json
import pandas as pd
import requests
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


DATA_URL = "https://s3.amazonaws.com/gupy5/production/companies/41683/emails/1679437007669/8408fe80-c80f-11ed-80da-7d3cd1fee4b4/log.txt"
PATH_EXPORT_DATA = "sre-intern-test"


def request_get_data(url: str):
    """
        Request in URL to get data.
    """
    
    response = requests.get(DATA_URL)
    
    if response.status_code == 200:
        data = response.text
        
        return data
    else:
        print(f"❌ Request Error - {response.status_code}")


def str_dict_to_list_dict(data: str) -> list:
    """
        Transform strings who are dictionary("str(list[dict])") in list[dict].
    """

    list_dict = []

    splited_data = data.split("\n")
    
    for item in splited_data:
        if item != '':
            json_object = json.loads(item.replace("'", "\""))
            list_dict.append(json_object)
    
    return list_dict


def list_dict_to_dataframe(data: list) -> pd.DataFrame:
    """
        Transform list[dict] in DataFrame.
    """
	
    df = pd.DataFrame.from_records(data)
    
    return df


def transform_type_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
        Transforms the type of columns in the DataFrame.
    """
    
    df["statusCode"] = df["statusCode"].astype(int)

    return df


def generate_summary_erros_success(df: pd.DataFrame) -> list:
    """
        Analyze data from DataFrame for generate new columns based on the analytics.
    """

    df["successCount"] = df.apply(lambda row: 1 if row.statusCode >= 200 and row.statusCode <= 399 else 0, axis = 1)
    df["errorCount"] = df.apply(lambda row: 1 if row.statusCode >= 400 and row.statusCode <= 599 else 0, axis = 1)


    df_summary = df.groupby(["path"])[["errorCount", "successCount"]].agg('sum').reset_index()


    list_dict = df_summary[["path",  "errorCount", "successCount"]].to_dict(orient = 'records')

    return list_dict


def prepare_data() -> list:
    """
        Organize functions for just get the data.
    """
    
    data = request_get_data(DATA_URL)
    splited_data = str_dict_to_list_dict(data=data)
    df = list_dict_to_dataframe(data=splited_data)
    df = transform_type_columns(df=df)
    summary = generate_summary_erros_success(df=df)
    
    return summary


def export_to_json(data: dict, path: str) -> None:
    """
        Generate file .json with the data.
    """

    with open(f"{path}/output.json", "w") as file:
        json.dump(data, file, indent=4)

    return None


def summary_in_terminal(data: dict) -> None:
    """
        Print output data in terminal.
    """

    print(
        json.dumps(data, indent=4)
    )

    return None


def read_args() -> None:
    """
        Construct Argparse and get options from CLI.
    """

    parser = argparse.ArgumentParser(description="Syncer")
    parser._action_groups.pop()

    options = parser.add_argument_group("Argumentos")

    options.add_argument(
        "-e", "--export",
        action="store_true",
        help="Export data to output file.",
        required=False
    )

    options.add_argument(
        "-s", "--summary",
        action="store_true",
        help="Print summary on terminal.",
        required=False
    )

    config_arg = parser.parse_args().__dict__


    if config_arg["export"]:
        data = prepare_data()
        export_to_json(data=data, path=PATH_EXPORT_DATA)

    if config_arg["summary"]:
        data = prepare_data()
        summary_in_terminal(data=data)


if  __name__ == "__main__":
    read_args()
