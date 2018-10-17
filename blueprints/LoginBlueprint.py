from flask import Blueprint,render_template
from forms import addForm,LoginForm
from classes.DB import DB

login_blueprint = Blueprint('login_blueprint', __name__)

@login_blueprint.route("/login", methods=['GET', 'POST'])
def login():
  form = LoginForm()
  return render_template('login.html', title = 'Login', form = form)