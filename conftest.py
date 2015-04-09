import pytest

from rest_framework.test import APIClient


@pytest.fixture()
def api_client(db):
    """
    A rest_framework api test client not auth'd.
    """
    client = APIClient()
    return client
