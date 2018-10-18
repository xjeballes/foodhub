from flask import Blueprint,render_template,request,redirect
from classes.DB import DB
from forms import addForm,LoginForm
import mysql.connector
from classes.RegistrationForm import RegistrationForm

register_blueprint = Blueprint('register_blueprint', __name__)
mydb = DB().conn()
mycursor = mydb.cursor()

@register_blueprint.route("/registration", methods=['GET', 'POST'])
def registration():
    form = RegistrationForm(request.form)
    global mydb,mycursor
    if request.method == 'POST' and form.validate():
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
        

            mycursor = mydb.cursor()
            mycursor.execute(sql, [username])
            
            myresult = mycursor.fetchone()
            print myresult
        except mysql.connector.Error as err:
            print(err)
    elif request.method == 'POST':
        return render_template('registration.html', form=form,error=True)

    return render_template('registration.html', form=form,)