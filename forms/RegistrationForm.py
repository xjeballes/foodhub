from wtforms import ValidationError, Form, BooleanField, StringField,SelectField, PasswordField, validators,RadioField
from classes.DB import DB

mydb = DB().conn()
print "Reg: ", mydb
mycursor = mydb.cursor()
def unique_username(form, field):
    if form.type.data == "owner":
        sql = "SELECT owner_id as id from owner where username=%s"
    else:
        sql = "SELECT user_id as id from customer where username=%s"

    
    
    mycursor.execute(sql, [field.data])
    result = mycursor.fetchall()
    mydb.commit()
    if(len(result) != 0):
        print "Validation Error: Username {} is already taken".format(field.data)
        raise ValidationError('Username {} is already taken.'.format(field.data))
    return True

def unique_email(form, field):
    if form.type.data == "owner":
        sql = "SELECT owner_id as id from owner where email=%s"
    else:
        sql = "SELECT user_id as id from customer where email=%s"

    
    mycursor = mydb.cursor()
    mycursor.execute(sql, [field.data])
    result = mycursor.fetchall()
    mydb.commit()
    if(len(result) != 0):
        print "Validation Error: Email{} is already taken".format(field.data)
        raise ValidationError('Email {} is already taken.'.format(field.data))
    return True
    
class RegistrationForm(Form):
    firstname = StringField('Firstname', [validators.DataRequired(),validators.Length(min=1, max=25,message="First Name must be between 1 and 25 characters long.")])
    lastname = StringField('Lastname', [validators.DataRequired(),validators.Length(min=1, max=25,message="Last Name must be between 1 and 25 characters long.")])
    gender = SelectField('Gender', choices=[('Male','Male'),('Female','Female')])
    contact_number =StringField('Contact Number', [validators.DataRequired(),validators.Length(min=11, max=11,message="Contact must be 11 characters long.")])
    username = StringField('Username', [validators.DataRequired(),validators.Length(min=1, max=25,message="Username must be between 1 and 25 characters long."),unique_username])
    email = StringField('Email Address', [validators.DataRequired(),validators.Length(min=6, max=35,message="Email must be between 6 and 35 characters long."),unique_email])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('cpassword', message='Passwords must match')
    ])
    cpassword = PasswordField('Repeat Password',[validators.DataRequired()])
    type = RadioField('',[validators.DataRequired(message="Please select account type.")],choices=[('customer','customer'),('owner','owner')])
    restaurant_name = StringField('Restaurant Name', [validators.Length(min=0, max=25,message="Restaurant Name must be between 1 and 25 characters long.")])
    restaurant_type = StringField('Restaurant Type', [validators.Length(min=0, max=25,message="Restaurant Type must be between 1 and 25 characters long.")])
    bio = StringField('Bio', [validators.Length(min=0, max=150,message="Bio must be between 1 and 150 characters long.")])
    locations = StringField('Locations', [validators.Length(min=0, max=25,message="Locations must be between 1 and 25 characters long.")])

