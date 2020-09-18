import requests
from .user import User
from .handle_request import RequestHandler
from settings import GET_USERS_URL

class Users:

    @classmethod
    def get_users(cls):
        json_response = RequestHandler.get_json(GET_USERS_URL)
        json_result = json_response['data']
        user_list = []
        for item in json_result:
            user = User(item['id'],
                        item['name'],
                        item['gender'],
                        item['email'],
                        item['created_at'],
                        item['updated_at'],
                        item['status'])
            user_list.append(user)
        return user_list

    @classmethod
    def get_user_response(cls, id):
        user_url = GET_USERS_URL + "/" + str(id)
        json_response = RequestHandler.get_json(user_url)
        return json_response

    @classmethod
    def user_exists(cls, user, user_list=[]):
        for item in user_list:
            if user.id == item.id:
                return True
        return False

if __name__ == "__main__":
    user = Users.get_user(15)
    print(user['code'])
    print(user['data'])