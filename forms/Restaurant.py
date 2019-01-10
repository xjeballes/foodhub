from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length,Email 


class addItem(FlaskForm):
	picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    itemname = StringField('Item Name', validators=[DataRequired(), Length(min=3, max=20)])
    price = StringField('Price', validators=[DataRequired()])
    submit = SubmitField('Enter')