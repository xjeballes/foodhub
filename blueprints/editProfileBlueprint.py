from flask import Blueprint,session,render_template,request,redirect,url_for
from classes.DB import DB
import mysql.connector
from forms.RegistrationForm import RegistrationForm
from classes.User import User
import mysql.connector


editProfile_blueprint = Blueprint('editProfile_blueprint', __name__)
mydb = DB().conn()
mycursor = mydb.cursor(dictionary=True)

@editProfile_blueprint.route("/editprofile", methods=['GET', 'POST'])
def editprofile():
    error = None
    user=session['user']
    print user
    sql = "SELECT lastname,firstname,gender,username,email,contact_number from customer WHERE user_id = %s"
        
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
        user_id = user['id']
        sql = "UPDATE customer SET firstname= %s, lastname= %s, username= %s,gender= %s,contact_number= %s, email= %s WHERE  user_id = %s"
        val = (firstname,lastname,username,gender,contact_number,email,user_id)
        mycursor.execute(sql, val)
        mydb.commit()
        sql1 = "SELECT user_id as id,firstname,lastname,gender,contact_number,username,email from customer where username=%s"
        
        mycursor.execute(sql1, [username])
        user = mycursor.fetchone()
        mydb.commit()
        session['user'] = user
        print user

        data = mycursor.fetchone ()
        return redirect(url_for('profile_blueprint.profile',title='Profile',data=data))

    return render_template('editprofile.html', form=form, data=data)