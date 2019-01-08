from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ReviewForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	content = TextAreaField('Review', validators=[DataRequired()])
	submit = SubmitField('Post')