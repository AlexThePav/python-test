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
    existing_user = User(15, "Dian Gunawan")

    assert Users.user_exists(existing_user, all_users), \
        f'User id {existing_user.id} does not exist.'

def test_api_get_user():
    logging.info("Running get user test")
    user = Users.get_user_response(id=15)
    assert user['code'] == 200

def test_api_get_user_not_found():
    logging.info("Running get user not found test")
    user = Users.get_user_response(id=0)
    assert user['code'] == 404