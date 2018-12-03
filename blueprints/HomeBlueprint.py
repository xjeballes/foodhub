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

	#sql = '''SELECT * from restaurant'''
	#mycursor.execute(sql,data)
	#data = mycursor.fetchall()

	return render_template('home.html', title = 'Home',user=user)
