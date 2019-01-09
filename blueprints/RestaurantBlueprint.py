from flask import Blueprint,render_template,session,redirect, request, url_for
from classes.DB import DB
import mysql.connector
from forms.RegistrationForm import RegistrationForm
from forms.ReviewForm import ReviewForm
from forms.SearchForm import SearchForm

mydb = DB().conn()
mycursor = mydb.cursor(dictionary=True) 
restaurant_blueprint = Blueprint('restaurant_blueprint', __name__)

@restaurant_blueprint.route("/rest/<string:name>", methods=['GET', 'POST'])
def rest(name):
	searchForm = SearchForm()

	name = name
	sql = "SELECT * FROM restaurant WHERE restaurant_name = %s or restaurant_name = %s "
	mycursor.execute(sql, (name,name))
	data = mycursor.fetchone ()
	print data
	user = None

	return render_template('restaurant_beforelogin.html', title = 'Restaurant', user=data, searchForm=searchForm)

#@restaurant_blueprint.route("/restaurant/<restaurant_id>", methods=['GET', 'POST'])
#def reserve(restaurant_id):
	#user = None
	#if 'user' in session: 
	#	user = session['user']
	#else:
	#	return redirect(url_for('login_blueprint.login'))

	#print user
	#restaurant_id=restaurant_id
	
	#sql = "SELECT restaurant_name,restaurant_type,bio,locations from restaurant WHERE restaurant_id = %s"
	#mycursor.execute(sql,restaurant_id)
	#data = mycursor.fetchone ()
	#print data
	#return render_template('restaurant_customer.html', title = 'Restaurant', user=data)

@restaurant_blueprint.route("/restaurant/<string:name>", methods=['GET', 'POST'])
def restaurantcus(name):
	searchForm = SearchForm()
	form = ReviewForm()
	name = name
	sql = "SELECT * FROM restaurant WHERE restaurant_name = %s or restaurant_name = %s "
	mycursor.execute(sql, (name,name))
	data = mycursor.fetchone ()
	user = None
	if 'user' in session:
		user = session['user']
	else:
		return redirect(url_for('login_blueprint.login'))


	sql = "SELECT * from restaurant r,owner o WHERE r.owner_id = o.owner_id AND o.owner_id = %s"
	mycursor.execute(sql,[user['id']])
	items = mycursor.fetchall ()

	

	return render_template('restaurant_customer.html', title = 'Restaurant', user=user, data=data, items=items, form=form, searchForm=searchForm)

@restaurant_blueprint.route("/<string:name>", methods=['GET', 'POST'])
def restaurant(name):
	searchForm = SearchForm()
	name = name
	sql = "SELECT * FROM restaurant WHERE restaurant_name = %s or restaurant_name = %s "
	mycursor.execute(sql, (name,name))
	data = mycursor.fetchone ()
	user = None
	if 'user' in session:
		user = session['user']
	else:
		return redirect(url_for('login_blueprint.login'))


	sql = "SELECT * from restaurant r,owner o WHERE r.owner_id = o.owner_id AND o.owner_id = %s"
	mycursor.execute(sql,[user['id']])
	items = mycursor.fetchall ()

	

	return render_template('restaurant_owner.html', title = 'Restaurant', user=user, data=data, items=items, searchForm=searchForm)


@restaurant_blueprint.route("/editrestaurant", methods=['GET', 'POST'])
def editrestaurant():
	searchForm = SearchForm()
	error = None
	user=session['user']
	print user
	sql = "SELECT owner.owner_id as id,firstname,lastname,gender,contact_number,username,email,restaurant_name,bio,'time' from owner,restaurant WHERE restaurant.owner_id == owner.restaurant_id && owner.owner_id = %s"
	mycursor.execute(sql,[user['id']])
	data = mycursor.fetchone ()

	form = RegistrationForm(request.form)
	if request.method == 'POST':
		restaurant_name = request.form["restaurant_name"]
		bio = request.form["bio"]
		locations = request.form["locations"]
		time = request.form["time"]
		contact_number = request.form["contact_number"]
		owner_id = user['id']
        #restaurant_id = 
        sql = "UPDATE restaurant SET restaurant_name= %s, bio= %s, 'time'= %s,contact_number= %s WHERE  owner_id = %s"
        val = (restaurant_name,bio,'time',contact_number,owner_id)
        mycursor.execute(sql, val)
        mydb.commit()
        sql1 = "SELECT restaurant_id as id,restaurant_name,bio,contact_number,'time' from restaurant where owner=%s"

        mycursor.execute(sql1, [user['id']])
        user = mycursor.fetchone()
        mydb.commit()
        session['user'] = user
        print user
        data = mycursor.fetchone ()
        return redirect(url_for('restaurant_blueprint.restaurant',title='Profile',user=data, searchForm=searchForm))

	return render_template('editrestaurant.html', form=form, user=data, searchForm=searchForm)