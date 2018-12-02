from flask import Flask, session, render_template, url_for, request, flash, redirect

from classes.DB import DB
import mysql.connector
from mysql.connector import errorcode
import os

##import blueprints
from blueprints.LoginBlueprint import login_blueprint
from blueprints.RegisterBlueprint import register_blueprint
from blueprints.HomeBlueprint import home_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfged123qwkjasdasddqwqd4'

#register blueprints
app.register_blueprint(login_blueprint)
app.register_blueprint(register_blueprint)
app.register_blueprint(home_blueprint)

@app.route("/")
def home():
	return render_template('home.html')

@app.route("/logout", methods=['GET', 'POST'])
def logout():
  if 'user' in session:
    session.pop('user')
  return redirect(url_for('home_blueprint.home'))

@app.route("/login", methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if request.method == 'POST':
    username = request.form["username"].upper()
    password = request.form["password"].upper()

    sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
    val = (username, password)
    mycursor.execute(sql, val)
    mydb.commit()


  return render_template('loginform.html', form=form  )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug = True)