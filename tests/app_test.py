from . import client


def test_hello(client):
    result = client.get('/')
    print(result.data)
    assert result == 'Hello world'
