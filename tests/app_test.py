def test_hello(client):
    result = client.get('/')
    assert 'Hello world' in str(result.data)
