import requests
from .user import User
from .handle_request import RequestHandler
from settings import GET_USERS_URL

class Users:

    def get_users(self):
        json_response = RequestHandler.get_json(GET_USERS_URL)
        json_result = json_response['result']
        user_list = []
        for item in json_result:
            user = User(item['id'],
                        item['first_name'],
                        item['last_name'],
                        item['gender'],
                        item['dob'],
                        item['email'],
                        item['phone'],
                        item['website'],
                        item['address'],
                        item['status'])
            user_list.append(user)
        return user_list

    def user_exists(self, user, user_list=[]):
        for item in user_list:
            if str(user.id) == item.id:
                return True
        return False