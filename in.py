from flask import Flask, render_template, url_for, request, flash, redirect
from login import LoginForm
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="mydatabase"
)

mycursor = mydb.cursor()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'omgod123qwkjasdasddqwqd4'


#Add student
@app.route("/")
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


if __name__ =='__main__':
    app.run(debug=True)