import pandas as pd

from app.index import (
    generate_summary_erros_success,
    list_dict_to_dataframe,
    request_get_data,
    str_dict_to_list_dict,
    transform_type_columns
)
from datatest import validate


def test_request_get_data():
    url = "https://sobre.quero.com"

    try:
        request_get_data(url=url)
        assert True
    except:
        assert False


def test_str_dict_to_list_dict():
    str_dict = "{'env': 'prod', 'path': '/path1', 'method': 'PUT'}"

    list_dict = str_dict_to_list_dict(data=str_dict)

    assert isinstance(list_dict, list)


def test_list_dict_to_dataframe():
    list_dict = [
        {"env": "prod", "path": "/path1", "method": "PUT"},
        {"env": "prod", "path": "/path1", "method": "PUT"},
        {"env": "prod", "path": "/path1", "method": "PUT"}
    ]

    df = list_dict_to_dataframe(data=list_dict)

    assert isinstance(df, pd.DataFrame)


def  test_transform_type_columns():
    list_dict = [
        {"env": "prod", "path": "/path1", "statusCode": "200"},
        {"env": "prod", "path": "/path1", "statusCode": "500"},
        {"env": "prod", "path": "/path1", "statusCode": "465"}
    ]

    df = pd.DataFrame.from_records(list_dict)
    df = transform_type_columns(df=df)

    validate(df["statusCode"], int)


def test_generate_summary_erros_success():
    list_dict = [
        {"path": "/path1", "statusCode": 200},
        {"path": "/path1", "statusCode": 500},
        {"path": "/path1", "statusCode": 465}
    ]

    df = pd.DataFrame.from_records(list_dict)

    response = generate_summary_erros_success(df=df)

    assert isinstance(response, list)
