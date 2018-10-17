from flask import Blueprint,render_template,request,redirect
from classes.DB import DB
from forms import addForm,LoginForm
import mysql.connector

register_blueprint = Blueprint('register_blueprint', __name__)
mydb = DB().conn()
mycursor = mydb.cursor()

@register_blueprint.route("/registration", methods=['GET', 'POST'])
def registration():
  form = addForm()
  if request.method == 'POST':
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    gender = request.form["gender"]
    contact_number = request.form["contact_number"]
    username= request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    

    if(request.form["type"] == "owner"):
        sql = "INSERT INTO customer ( firstname,lastname,gender,contact_number,username, email, password) VALUES (%s, %s, %s, %s, %s, %s,%s)"
    else:
        sql = "INSERT INTO owner ( firstname,lastname,gender,contact_number,username, email, password) VALUES (%s, %s, %s, %s, %s, %s,%s)"
    
    val = (firstname,lastname,gender,contact_number,username,email,password)
    try:
        mycursor.execute(sql, val)
        mydb.commit()

        if(request.form["type"] == "owner"):
            sql = "SELECT firstname,lastname,gender,contact_number,username,email from owner where username=%s"
        else:
            sql = "SELECT firstname,lastname,gender,contact_number,username,email from customer where username=%s"
       

        mycursor.execute(sql, [username])
        
        myresult = mycursor.fetchone()
        for firstname,lastname in myresult:
            print(firstname)
        mydb.commit()
    except mysql.connector.Error as err:
        print(err)

  return render_template('registration.html', form=form)