from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length,Email,EqualTo

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password',validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')
	
    #def validate_username(self, field):
      #  if User.query.filter_by(username=field.data).first() is None:
        #    raise ValidationError('Username is not registered')

