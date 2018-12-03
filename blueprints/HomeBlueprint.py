from flask import Blueprint,render_template,session, request, url_for
from classes.DB import DB
from classes.User import User
import mysql.connector


mydb = DB().conn()
mycursor = mydb.cursor(dictionary=True) 
home_blueprint = Blueprint('home_blueprint', __name__)

@home_blueprint.route("/", methods=['GET', 'POST'])
def home():
	user = None
	if 'user' in session:
		user = session['user']
<<<<<<< HEAD

	#sql = '''SELECT * from restaurant'''
	#mycursor.execute(sql,data)
	#data = mycursor.fetchall()

	return render_template('home.html', title = 'Home',user=user)
=======
	return render_template('home.html', title = 'Home',user=user)
>>>>>>> dcd3fa4953a406e7bd0d87ceefc80b868b3d274c
