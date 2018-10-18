from flask import Blueprint,render_template,session
from classes.DB import DB

home_blueprint = Blueprint('home_blueprint', __name__)

@home_blueprint.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html', title = 'Home')