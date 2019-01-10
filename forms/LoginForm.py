from flask_wtf import FlaskForm
from wtforms import ValidationError, Form, BooleanField, StringField,SelectField, PasswordField, validators,RadioField
from wtforms.validators import DataRequired, Length,Email #,EqualTo
from classes.DB import DB

mydb = DB().conn()

mycursor = mydb.cursor()
def unique_username(form, field):
    if form.types.data == "owner":
        sql = "SELECT owner_id as id from owner where username=%s"
    else:
        sql = "SELECT customer_id as id from customer where username=%s"

    
    
    mycursor.execute(sql, [field.data])
    result = mycursor.fetchall()
    mydb.commit()
    if(len(result) != 0):
        print "Validation Error: Username {} is already taken".format(field.data)
        raise ValidationError('Username {} is already taken.'.format(field.data))
    return True

def unique_email(form, field):
    if form.types.data == "owner":
        sql = "SELECT owner_id as id from owner where email=%s"
    else:
        sql = "SELECT customer_id as id from customer where email=%s"

    
    mycursor = mydb.cursor()
    mycursor.execute(sql, [field.data])
    result = mycursor.fetchall()
    mydb.commit()
    if(len(result) != 0):
        print "Validation Error: Email{} is already taken".format(field.data)
        raise ValidationError('Email {} is already taken.'.format(field.data))
    return True
    
class LoginForm(Form):
    username = StringField('Username:', [validators.DataRequired(),validators.Length(min=5, max=25,message="Username must be between 5 and 25 characters long."),unique_username])
    password = PasswordField('Password:', [validators.DataRequired(),validators.Length(min=5, max=25,message="Username must be between 5 and 25 characters long."),unique_username])
    types = RadioField('',[validators.DataRequired(message="Please select account type.")],choices=[('customer','customer'),('owner','owner')])

