from flask import Blueprint,session,render_template,request,redirect,url_for
from classes.DB import DB
import mysql.connector
from forms.RegistrationForm import RegistrationForm
from classes.User import User
import mysql.connector
from flask_bcrypt import Bcrypt
from forms.SearchForm import SearchForm

bcrypt = Bcrypt()

register_blueprint = Blueprint('register_blueprint', __name__)
mydb = DB().conn()
mycursor = mydb.cursor(dictionary=True)

@register_blueprint.route("/registration/customer", methods=['GET', 'POST'])
def registration_customer():
    searchForm = SearchForm()
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
        sql1 = "SELECT customer_id as id,firstname,lastname,gender,contact_number,username,email from customer where username=%s"
        
        mycursor.execute(sql1, [username])
        user = mycursor.fetchone()
        mydb.commit()
        session['user'] = user
        return redirect(url_for('home_blueprint.homecus'))

    elif request.method == 'POST':
        return render_template('register_customer.html', form=form,error=True, title='Register', searchForm=searchForm)

    return render_template('register_customer.html', form=form, title= 'Register', searchForm=searchForm)


@register_blueprint.route("/registration/owner", methods=['GET', 'POST'])

def registration_owner():
    searchForm = SearchForm()
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
        time = request.form["time"]
        restaurant_location = request.form["restaurant_location"]



        sql1 = "INSERT INTO owner ( firstname,lastname,gender,contact_number,username, email, password) VALUES (%s, %s, %s, %s, %s, %s,%s)"
        val1 = (firstname,lastname,gender,contact_number,username,email,password)
        mycursor.execute(sql1, val1)
        mydb.commit()  

        sql3 = "SELECT owner_id as id,firstname,lastname,gender,contact_number,username,email from owner where username=%s"
        mycursor.execute(sql3, [username])
        user = mycursor.fetchone()

        mydb.commit()
        session['user'] = user

        sql2 = "INSERT INTO restaurant ( restaurant_name,restaurant_type,bio,time,owner_id) VALUES (%s, %s, %s, %s, %s)"
        val2 = (restaurant_name,restaurant_type,bio,time, user['id'])
        mycursor.execute(sql2, val2)
        mydb.commit()  

        #sql5 = "SELECT restaurant_id as id where restaurant_name=%s"
        #mycursor.execute(sql5, [restaurant_name])
        #restaurant = mycursor.fetchone()

        #sql4 = "INSERT INTO location ( restaurant_location,restaurant_id) VALUES (%s, %s)"
        #val4 = (restaurant_location, restaurant['id'])
        #mycursor.execute(sql4, val4)
        #mydb.commit()  
        
        return redirect(url_for('home_blueprint.home'))

    elif request.method == 'POST':
        return render_template('register_owner.html', form=form,error=True, title='Register', searchForm=searchForm)

    return render_template('register_owner.html', form=form, title='Register', searchForm=searchForm)

