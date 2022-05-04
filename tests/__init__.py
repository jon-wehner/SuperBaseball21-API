import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.app.test_client() as client:
        yield client
