from flask import Blueprint,render_template,session,redirect,url_for
from forms import addForm,LoginForm
from classes.DB import DB

login_blueprint = Blueprint('login_blueprint', __name__)

@login_blueprint.route("/login", methods=['GET', 'POST'])
def login():
  if 'user' in session:
    print 'Found user in session: ', session['user']
    return redirect(url_for('home_blueprint.home'))
  form = LoginForm()
  return render_template('login.html', title = 'Login', form = form)