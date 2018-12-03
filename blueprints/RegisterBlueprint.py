from flask import Blueprint,session,render_template,request,redirect,url_for
from classes.DB import DB
import mysql.connector
from forms.RegistrationForm import RegistrationForm
from classes.User import User
import mysql.connector
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

register_blueprint = Blueprint('register_blueprint', __name__)
mydb = DB().conn()
mycursor = mydb.cursor(dictionary=True)

@register_blueprint.route("/registration/customer", methods=['GET', 'POST'])
def registration_customer():
    if('user' in session):
        print 'Found user in session: ', session['user']
        return redirect(url_for('login_blueprint.login'))
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        gender = request.form["gender"]
        contact_number = request.form["contact_number"]
        username= request.form["username"]
        email = request.form["email"]
        password = bcrypt.generate_password_hash(request.form["password"]) 

        sql = "INSERT INTO customer ( firstname,lastname,gender,contact_number,username, email, password) VALUES (%s, %s, %s, %s, %s, %s,%s)"
        val = (firstname,lastname,gender,contact_number,username,email,password)
        mycursor.execute(sql, val)
        mydb.commit()  
        sql1 = "SELECT user_id as id,firstname,lastname,gender,contact_number,username,email from customer where username=%s"
        
        mycursor.execute(sql1, [username])
        user = mycursor.fetchone()
        mydb.commit()
        session['user'] = user
        return redirect(url_for('home_blueprint.home'))

    elif request.method == 'POST':
        return render_template('register_customer.html', form=form,error=True, title='Register')

    return render_template('register_customer.html', form=form, title= 'Register')


@register_blueprint.route("/registration/owner", methods=['GET', 'POST'])

def registration_owner():
    if('user' in session):
        print 'Found user in session: ', session['user']
        return redirect(url_for('login_blueprint.login'))

    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        gender = request.form["gender"]
        contact_number = request.form["contact_number"]
        username= request.form["username"]
        email = request.form["email"]
        password = bcrypt.generate_password_hash(request.form["password"])
        restaurant_name = request.form["restaurant_name"]
        restaurant_type = request.form["restaurant_type"]
        bio = request.form["bio"]
        locations = request.form["locations"]


        sql1 = "INSERT INTO owner1 ( firstname,lastname,gender,contact_number,username, email, password, restaurant_name,restaurant_type,bio,locations) VALUES (%s, %s, %s, %s, %s, %s,%s,%s, %s, %s,%s)"
        val1 = (firstname,lastname,gender,contact_number,username,email,password,restaurant_name,restaurant_type,bio,locations)
        mycursor.execute(sql1, val1)
        mydb.commit()  

        # sql2 = "INSERT INTO restaurant ( restaurant_name,restaurant_type,bio,locations) VALUES (%s, %s, %s, %s)"
        # val2 = (restaurant_name,restaurant_type,bio,locations)
        # mycursor.execute(sql2, val2)
        # mydb.commit()  

        sql3 = "SELECT owner_id as id,firstname,lastname,gender,contact_number,username,email, restaurant_name,restaurant_type,bio,locations from owner1 where username=%s"
        mycursor.execute(sql3, [username])
        user = mycursor.fetchone()

        mydb.commit()
        session['user'] = user
        return redirect(url_for('home_blueprint.home'))

    elif request.method == 'POST':
        return render_template('register_owner.html', form=form,error=True, title='Register')

    return render_template('register_owner.html', form=form, title='Register')

