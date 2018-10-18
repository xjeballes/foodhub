from wtforms import Form, BooleanField, StringField,SelectField, PasswordField, validators,RadioField

class RegistrationForm(Form):
    firstname = StringField('Firstname', [validators.Length(min=1, max=25,message="First Name must be between 1 and 25 characters long.")])
    lastname = StringField('Lastname', [validators.Length(min=1, max=25,message="Last Name must be between 1 and 25 characters long.")])
    gender = SelectField('Gender', choices=[('Male','Male'),('Female','Female')])
    contact_number =StringField('Contact Number', [validators.Length(min=11, max=11,message="Contact must be 11 characters long.")])
    username = StringField('Username', [validators.Length(min=1, max=25,message="Username must be between 1 and 25 characters long.")])
    email = StringField('Email Address', [validators.Length(min=6, max=35,message="Email must be between 6 and 35 characters long.")])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('cpassword', message='Passwords must match')
    ])
    cpassword = PasswordField('Repeat Password')
    type = RadioField('',[validators.DataRequired(message="Please select account type.")],choices=[('customer','customer'),('owner','owner')])