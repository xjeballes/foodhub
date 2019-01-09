from flask import Blueprint,render_template,session, request, url_for
from classes.DB import DB
from classes.User import User
import mysql.connector
from forms.SearchForm import SearchForm


mydb = DB().conn()
mycursor = mydb.cursor(dictionary=True) 
home_blueprint = Blueprint('home_blueprint', __name__)

@home_blueprint.route("/home", methods=['GET', 'POST'])
def home():
	searchForm = SearchForm()
	sql = "SELECT * from restaurant"
	mycursor.execute(sql)
	data = mycursor.fetchall()
	
	user = None
	if 'user' in session:
		user = session['user']
		sql = "SELECT * from restaurant r,owner o WHERE r.owner_id = o.owner_id AND o.owner_id = %s"
		mycursor.execute(sql,[user['id']])
		items = mycursor.fetchall ()
		return render_template('home.html', title = 'Home',user=user, data=data, items=items, searchForm=searchForm)
	
	return render_template('home.html', title = 'Home',user=user, data=data, searchForm=searchForm)



@home_blueprint.route("/home/cus", methods=['GET', 'POST'])
def homecus():
	searchForm = SearchForm()
	sql = "SELECT * from restaurant"
	mycursor.execute(sql)
	data = mycursor.fetchall()
	
	user = None
	if 'user' in session:
		user = session['user']

	print user
	

	return render_template('homecus.html', title = 'Home',user=user, data=data, searchForm=searchForm)

