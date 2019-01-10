import json
import os

class User(): 
    id = None
    firstname = None
    lastname = None
    gender = None
    username  = None
    email = None
    contact_number = None
    password = None
    type = None
    def __init__(self,id = None,firstname = None,lastname = None,gender = None,contact_number = None,username  = None,email = None,type = None, password= None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.username  = username
        self.email = email
        self.contact_number = contact_number
        self.type = type
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn