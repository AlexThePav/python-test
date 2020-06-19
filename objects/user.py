class User:
    def __init__(self, id, first_name, last_name, gender='', 
                dob='', email='', phone='', website='', 
                address='', status=''):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.dob = dob
        self.email = email
        self.phone = phone
        self.website = website
        self.address = address
        self.status = status
    
    def __repr__(self):
        return f"{self.id} - {self.first_name} {self.last_name}"
