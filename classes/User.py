

class User():
    id = None
    firstname = None
    lastname = None
    gender = None
    username  = None
    email = None
    contact_number = None
    type = None
    def __init__(self,id = None,firstname = None,lastname = None,gender = None,username  = None,email = None,contact_number = None,type = None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.username  = username
        self.email = email
        self.contact_number = contact_number
        self.type = type