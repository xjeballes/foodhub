from flask import Blueprint,render_template,session, request, url_for
from classes.DB import DB

mydb = DB().conn()
mycursor = mydb.cursor(dictionary=True) 
restaurant_blueprint = Blueprint('restaurant_blueprint', __name__)

@restaurant_blueprint.route("/restaurant", methods=['GET', 'POST'])
def restaurant():
	user = None
	if 'user' in session:
		user = session['user']
	else:
		return redirect(url_for('login_blueprint.login'))

	print user
	sql = "SELECT restaurant_name,restaurant_type,bio,locations from owner1 WHERE owner_id = %s"
	mycursor.execute(sql,[user['id']])
	data = mycursor.fetchone ()
	return render_template('restaurant.html', title = 'Restaurant', user=data)
