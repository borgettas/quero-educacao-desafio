from app.index import (
    request_get_data,
    list_str_dict_to_list_dict
)


def test_request_get_data():
    url = "https://sobre.quero.com"

    try:
        request_get_data(url=url)
        assert True
    except:
        assert False


def test_list_str_dict_to_list_dict():
    str_dict = "{'env': 'prod', 'path': '/path1', 'method': 'PUT'}"

    try:
        list_str_dict_to_list_dict(data=str_dict)
        assert True
    except:
        assert False