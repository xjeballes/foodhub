from flask import Flask, render_template, url_for, request, flash, redirect
import mysql.connector
import os
from forms import addForm,LoginForm
from mysql.connector import errorcode
from blueprints.LoginBlueprint import login_blueprint
from classes.DB import DB

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfged123qwkjasdasddqwqd4'
#register login blueprint
app.register_blueprint(login_blueprint)

mydb = DB()
mycursor = mydb.cursor()
@app.route("/login")
@app.route("/registration", methods=['GET', 'POST'])
def registration():
  form = addForm()
  if request.method == 'POST':
    lname = request.form["lname"]
    fname = request.form["fname"]
    email = request.form["email"]
    password = request.form["password"]
    cpassword = request.form["cpassword"]
    number = request.form["number"]

    sql = "INSERT INTO student_list (lastname, firstname, email, password, confirmpassword, contact_number) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (lname,fname,email,password,cpassword,number)
    mycursor.execute(sql, val)
    mydb.commit()

  return render_template('registration.html', form=form)



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug = True)