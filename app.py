from flask import Flask, session, render_template, url_for, request, flash, redirect
from classes.DB import DB
import mysql.connector
from mysql.connector import errorcode
import os 
from forms.SearchForm import SearchForm

##import blueprints
from blueprints.LoginBlueprint import login_blueprint
from blueprints.RegisterBlueprint import register_blueprint
from blueprints.HomeBlueprint import home_blueprint
from blueprints.ProfileBlueprint import profile_blueprint
from blueprints.editProfileBlueprint import editProfile_blueprint
from blueprints.RestaurantBlueprint import restaurant_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfged123qwkjasdasddqwqd4'

mydb = DB().conn()
mycursor = mydb.cursor(dictionary=True)
#register blueprints
app.register_blueprint(login_blueprint)
app.register_blueprint(register_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(profile_blueprint)
app.register_blueprint(editProfile_blueprint)
app.register_blueprint(restaurant_blueprint)

@app.route("/")
def location():
  return render_template('location.html')
@app.route("/home")
def home():
  return render_template('home.html')

@app.route("/register")
def register():
  searchForm = SearchForm()
  return render_template('register.html', searchForm=searchForm)

@app.route("/logout", methods=['GET', 'POST'])
def logout():
  if 'user' in session:
    session.pop('user')
  return redirect(url_for('home_blueprint.home'))

#===== SEARCH ===============================================================
@app.route("/search", methods=['GET', 'POST'])
def search():
  searchForm = SearchForm()
  user = session['user']
  if request.method == 'POST' and searchForm.validate_on_submit():
    resto = request.form['resto']
    sql = '''SELECT * FROM restaurant WHERE restaurant_name LIKE "%'''+resto+'''%" or restaurant_type LIKE "%'''+resto+'''%"'''
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print result

    return render_template('search.html', searchForm=searchForm, user=user, result=result)
  return render_template('search.html', searchForm=searchForm, user=user)
#===== SEARCH ===============================================================

@app.route("/about")
def about():
  user = None 
  if 'user' in session:
	user = session['user']
  return render_template('about.html', title= 'About', user=user)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug = True)