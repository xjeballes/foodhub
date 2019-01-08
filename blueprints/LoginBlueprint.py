from flask import Blueprint,render_template,session,redirect,url_for,request
from forms.LoginForm import LoginForm
from classes.DB import DB
from flask_bcrypt import Bcrypt
from classes.User import User 
from forms.SearchForm import SearchForm
bcrypt = Bcrypt()
mydb = DB().conn()
mycursor = mydb.cursor(dictionary=True) 
login_blueprint = Blueprint('login_blueprint', __name__)

@login_blueprint.route("/login", methods=['GET', 'POST'])
def login():
  #if 'user' in session:
  # print 'Found user in session: ', session['user']
  #  return redirect(url_for('home_blueprint.home'))
  searchForm = SearchForm()
  error = None
  form = LoginForm()
  if request.method == 'POST':

    username = request.form["username"]
    password = request.form["password"]
    types = request.form["types"]

    if types == "customer":
    	sql = "SELECT customer_id as id,firstname,lastname,gender,contact_number,username,email,password from customer where username=%s"
    else:
      sql = "SELECT owner_id as id,firstname,lastname,gender,contact_number,username,email,password from owner where username=%s"
    mycursor.execute(sql, [username])
    result = mycursor.fetchone()
    #check if password matches
    if result:
    	if bcrypt.check_password_hash(result['password'],password) and types == "customer":
    		del result['password']
    		session['user'] = result
    		return redirect(url_for('home_blueprint.homecus'))
    	elif bcrypt.check_password_hash(result['password'],password) and types == "owner":
    		del result['password']
    		session['user'] = result
    		return redirect(url_for('home_blueprint.home'))
    	else:
    		error = "Username and password did not match."
    else:
		  error = "Account does not exist."


  return render_template('loginform.html', title = 'Login', form = form, error=error, searchForm=searchForm)