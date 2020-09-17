import logging
from scripts.utils import logger
from scripts.fixtures import all_users
from objects.users import Users
from objects.user import User

def test_api_new_user(all_users):
    logging.info("Running new user test")
    new_user = User(1900, "John Doe")

    assert not Users.user_exists(new_user, all_users)

def test_api_existing_user(all_users):
    logging.info("Running existing user test")
    existing_user = User(1816, "Kelvin Gutkowski")

    assert Users.user_exists(existing_user, all_users), \
        f'User id {existing_user.id} does not exist.'