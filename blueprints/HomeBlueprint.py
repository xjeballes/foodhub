from flask import Blueprint,render_template,session
from classes.DB import DB

home_blueprint = Blueprint('home_blueprint', __name__)

@home_blueprint.route("/home", methods=['GET', 'POST'])
def home():
	user = None
	if 'user' in session:
		user = session['user']
	return render_template('home.html', title = 'Home',user=user)