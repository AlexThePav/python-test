import requests
from requests.auth import AuthBase

from settings import ACCESS_TOKEN

class TokenAuth(AuthBase):
    """Custom authentication scheme"""

    def __init__(self, token):
        self.token = token
    
    def __call__(self, r):
        """Attach API token to custom auth header"""
        r.headers['Authorization'] = f'Bearer {self.token}'
        return r
    
class RequestHandler:
    """Custom request handler"""

    @staticmethod
    def get_json(url):
        response = requests.get(url, auth=TokenAuth(ACCESS_TOKEN))
        json_response = response.json()
        return json_response