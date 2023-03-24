from app.index import request_get_data

def test_request_get_data():
    url = "https://sobre.quero.com"

    try:
        request_get_data(url=url)
        assert True
    except:
        assert False