import pytest

from objects.users import Users

@pytest.fixture
def all_users():
    '''
    Gets all users from endpoint specified in settings.py
    '''
    yield Users.get_users()