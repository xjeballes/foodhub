from flask_wtf import FlaskForm
from wtforms import StringField
from classes.DB import DB

mydb = DB().conn()

mycursor = mydb.cursor()

class SearchForm(FlaskForm):
    resto = StringField('Resto')
    