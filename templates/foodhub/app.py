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


@app.route("/logout", methods=['GET', 'POST'])
def logout():
  session.pop('user')
  return render_template('home.html', title = 'Home')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug = True)