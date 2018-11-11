from flask import Blueprint,render_template,session
from classes.DB import DB
from classes.User import User
import mysql.connector


profile_blueprint = Blueprint('profile_blueprint', __name__)
mydb = DB().conn()
mycursor = mydb.cursor(dictionary=True)
@profile_blueprint.route("/profile", methods=['GET', 'POST'])
def profile():
	user=session['user']
	print user
	sql = "SELECT lastname,firstname,username,email,contact_number from customer WHERE user_id = %s"
    	mycursor.execute(sql,[user['id']])
	#mycursor.execute ("SELECT lastname,firstname,username,email,contact_number from customer wheare user_id= %s")
	data = mycursor.fetchone ()
	return render_template('profile.html', title = 'Profile', data=data)
