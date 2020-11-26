import keyword
from collections import abc

class User:
    def __init__(self, id, name, gender='', 
                email='', created_at='', updated_at='', 
                status=''):
        self.id = id
        self.name = name
        self.gender = gender
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at
        self.status = status
    
    def __repr__(self):
        return f"{self.id} - {self.name}"


class CustomUser:
    """ 
    A read-only façade for navigating a JSON-like object
    using attribute notation
    """
    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg
        
    def __init__(self, args):
        self.__data = {}
        for key, value in args.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value
    
    def __getattr__(self, name: str):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return CustomUser(self.__data[name])

    def __repr__(self):
        return f"{self.id} - {self.name}"
