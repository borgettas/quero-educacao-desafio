from app.index import (
    list_dict_to_dataframe,
    request_get_data,
    str_dict_to_list_dict
)


def test_request_get_data():
    url = "https://sobre.quero.com"

    try:
        request_get_data(url=url)
        assert True
    except:
        assert False


def test_str_dict_to_list_dict():
    str_dict = "{'env': 'prod', 'path': '/path1', 'method': 'PUT'}"

    try:
        str_dict_to_list_dict(data=str_dict)
        assert True
    except:
        assert False


def test_list_dict_to_dataframe():
    list_dict = [
        {"env": "prod", "path": "/path1", "method": "PUT"},
        {"env": "prod", "path": "/path1", "method": "PUT"},
        {"env": "prod", "path": "/path1", "method": "PUT"}
    ]

    try:
        list_dict_to_dataframe(data=list_dict)
        assert True
    except:
        assert  False