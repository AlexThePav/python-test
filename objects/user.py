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
        return f"{self.id} - {self.first_name} {self.last_name}"
