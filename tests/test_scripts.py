import logging
from scripts.utils import logger
from objects.users import Users
from objects.user import User

def test_api_new_user():
    logging.info("Running new user test")
    users = Users()
    users_list = users.get_users()
    new_user = User(1900, "John", "Doe")

    assert not users.user_exists(new_user, users_list)

def test_api_existing_user():
    logging.info("Running existing user test")
    users = Users()
    users_list = users.get_users()
    existing_user = User(1816, "Kelvin", "Gutkowski")

    assert users.user_exists(existing_user, users_list), \
        f'User id {existing_user.id} does not exist.'