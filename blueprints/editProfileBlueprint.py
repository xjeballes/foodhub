from flask import Blueprint,session,render_template,request,redirect,url_for
from classes.DB import DB
import mysql.connector
from forms.RegistrationForm import RegistrationForm
from classes.User import User
import mysql.connector

 
editProfile_blueprint = Blueprint('editProfile_blueprint', __name__)
mydb = DB().conn()
mycursor = mydb.cursor(dictionary=True)

@editProfile_blueprint.route("/editcustomer", methods=['GET', 'POST'])
def editcustomer():
    error = None
    user=session['user']
    print user
    sql = "SELECT lastname,firstname,gender,username,email,contact_number from customer WHERE customer_id = %s"
        
    mycursor.execute(sql,[user['id']])
    data = mycursor.fetchone ()

    form = RegistrationForm(request.form)
    if request.method == 'POST':
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        username = request.form["username"]
        gender = request.form["gender"]
        email = request.form["email"]
        contact_number = request.form["contact_number"]
        customer_id = user['id']
        sql = "UPDATE customer SET firstname= %s, lastname= %s, username= %s,gender= %s,contact_number= %s, email= %s WHERE  customer_id = %s"
        val = (firstname,lastname,username,gender,contact_number,email,customer_id)
        mycursor.execute(sql, val)
        mydb.commit()
        sql1 = "SELECT customer_id as id,firstname,lastname,gender,contact_number,username,email from customer where username=%s"
        
        mycursor.execute(sql1, [username])
        user = mycursor.fetchone()
        mydb.commit()
        session['user'] = user
        print user

        data = mycursor.fetchone ()
        return redirect(url_for('profile_blueprint.profile',title='Profile',user=data))

    return render_template('editprofile.html', form=form, user=data)


@editProfile_blueprint.route("/editowner", methods=['GET', 'POST'])
def editowner():
    error = None
    user=session['user']
    print user
    sql = "SELECT lastname,firstname,gender,username,email,contact_number from owner WHERE owner_id = %s"
        
    mycursor.execute(sql,[user['id']])
    data = mycursor.fetchone ()

    form = RegistrationForm(request.form)
    if request.method == 'POST':
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        username = request.form["username"]
        gender = request.form["gender"]
        email = request.form["email"]
        contact_number = request.form["contact_number"]
        owner_id = user['id']
        sql = "UPDATE owner SET firstname= %s, lastname= %s, username= %s,gender= %s,contact_number= %s, email= %s WHERE  owner_id = %s"
        val = (firstname,lastname,username,gender,contact_number,email,owner_id)
        mycursor.execute(sql, val)
        mydb.commit()
        sql1 = "SELECT owner_id as id,firstname,lastname,gender,contact_number,username,email from owner where username=%s"
        
        mycursor.execute(sql1, [username])
        user = mycursor.fetchone()
        mydb.commit()
        session['user'] = user
        print user

        data = mycursor.fetchone ()
        return redirect(url_for('profile_blueprint.profile',title='Profile',user=data))

    return render_template('editprofile.html', form=form, user=data)