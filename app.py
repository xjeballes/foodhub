from flask import Flask, session, render_template, url_for, request, flash, redirect
from classes.DB import DB
import mysql.connector
from mysql.connector import errorcode
import os 

##import blueprints
from blueprints.LoginBlueprint import login_blueprint
from blueprints.RegisterBlueprint import register_blueprint
from blueprints.HomeBlueprint import home_blueprint
from blueprints.ProfileBlueprint import profile_blueprint
from blueprints.editProfileBlueprint import editProfile_blueprint
from blueprints.RestaurantBlueprint import restaurant_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfged123qwkjasdasddqwqd4'

#register blueprints
app.register_blueprint(login_blueprint)
app.register_blueprint(register_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(profile_blueprint)
app.register_blueprint(editProfile_blueprint)
app.register_blueprint(restaurant_blueprint)
@app.route("/")
def home():
  return render_template(restaurant.html)

@app.route("/logout", methods=['GET', 'POST'])
def logout():
  if 'user' in session:
    session.pop('user')
  return redirect(url_for('home_blueprint.home'))

@app.route("/search", methods=['GET', 'POST'])
def search():
  form = searchform()
  if request.method == 'POST':
    restaurant = request.form["restaurant"]
    sql = "SELECT * FROM restaurant where restaurant_name=%s restaurant_id=%d restaurant_type = %s locations = %s"
    adr = (restaurant, restaurant, restaurant, restaurant)
    mycursor.execute(sql, adr)
    result = mycursor.fetchall()
    return render_template('louie.html', result=restaurant)
  return render_template('search.html', form=form)

@app.route("/about")
def about():
  user = None 
  if 'user' in session:
	user = session['user']
  return render_template('about.html', title= 'About', user=user)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug = True)