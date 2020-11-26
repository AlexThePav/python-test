from .user import CustomUser
from .handle_request import RequestHandler
from settings import GET_USERS_URL

class Users:

    @staticmethod
    def get_users():
        json_response = RequestHandler.get_json(GET_USERS_URL)
        json_result = json_response['data']
        user_list = []
        for item in json_result:
            user = CustomUser(item)
            user_list.append(user)
        return user_list

    @staticmethod
    def get_user_response(id):
        user_url = GET_USERS_URL + "/" + str(id)
        json_response = RequestHandler.get_json(user_url)
        return json_response

    @staticmethod
    def user_exists(user, user_list=[]):
        for item in user_list:
            if user.id == item.id:
                return True
        return False



if __name__ == "__main__":
    user_list = Users.get_users()
    existing_user = CustomUser(15, "Dian Gunawan")
    print(Users.user_exists(existing_user, user_list))
