from flask import Blueprint,render_template,session
from classes.DB import DB
from classes.User import User
import mysql.connector
from werkzeug.utils import secure_filename
import uuid

path = 'uploads/pic'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def hash_filename(filename):
    filename = secure_filename(filename)
    ext = filename.rsplit('.', 1)[1].lower()
    return str(uuid.uuid4())+'.'+ext

profile_blueprint = Blueprint('profile_blueprint', __name__)
mydb = DB().conn()
mycursor = mydb.cursor(dictionary=True)
@profile_blueprint.route("/profile", methods=['GET', 'POST'])
def profile():
	if 'user' in session:
		user=session['user']
	else:
		return redirect(url_for('login_blueprint.login'))
		
	print user
	#sql = "SELECT column_name from INFORMATION_SCHEMA.COLUMNS where column_name = %s"
	#mycursor.execute(sql,[user['username']])
	#user_type = mycursor.fetchone()
	#print user_type
	# sql = "SELECT lastname,firstname,gender,username,email,contact_number from customer WHERE user_id = %s"
    	
 #    	mycursor.execute(sql,[user['id']])
	# data = mycursor.fetchone ()
	return render_template('_profile.html', title = 'Profile', user=user)
	