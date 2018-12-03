from flask import Blueprint,render_template,session,redirect,url_for,request
from forms.LoginForm import addForm,LoginForm
from classes.DB import DB
from flask_bcrypt import Bcrypt
from classes.User import User 
bcrypt = Bcrypt()
mydb = DB().conn()
mycursor = mydb.cursor(dictionary=True) 
login_blueprint = Blueprint('login_blueprint', __name__)

@login_blueprint.route("/login", methods=['GET', 'POST'])
def login():
  if 'user' in session:
    print 'Found user in session: ', session['user']
    return redirect(url_for('home_blueprint.home'))

  error = None
  if request.method == 'POST':
    username = request.form["username"]
    password = request.form["password"]
    type = request.form["type"]

    if type == "customer":
    	 sql = "SELECT user_id as id,firstname,lastname,gender,contact_number,username,email,password from customer where username=%s"
    else:
         sql = "SELECT owner_id as id,firstname,lastname,gender,contact_number,username,email,password from owner where username=%s"
    mycursor.execute(sql, [username])
    result = mycursor.fetchone()
    #check if password matches
    if result:
    	if bcrypt.check_password_hash(result['password'],password):
    		del result['password']
    		session['user'] = result
    		return redirect(url_for('home_blueprint.home'))
    	else:
    		error = "Username and password did not match."
    else:
		error = "Account does not exist."


  form = LoginForm()
  return render_template('loginform.html', title = 'Login', form = form,error=error)