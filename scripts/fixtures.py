import pytest

@pytest.fixture
def all_users():
    '''
    Gets all users from endpoint specified in settings.py
    '''
    from objects.users import Users
    yield Users.get_users()