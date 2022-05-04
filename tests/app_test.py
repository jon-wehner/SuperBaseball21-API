from app import hello
from . import client


def test_hello():
    result = client.get('/')
    assert result == 'Hello World'
