from flask import Blueprint,session,render_template,request,redirect,url_for
from classes.DB import DB
import mysql.connector
from forms.RegistrationForm import RegistrationForm
from classes.User import User
import mysql.connector


register_blueprint = Blueprint('register_blueprint', __name__)
mydb = DB().conn()
mycursor = mydb.cursor()
@register_blueprint.route("/registration", methods=['GET', 'POST'])
def registration():
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
        password = request.form["password"]
        type=request.form['type']
        try:

            if(type == "owner"):
                sql = "INSERT INTO owner ( firstname,lastname,gender,contact_number,username, email, password) VALUES (%s, %s, %s, %s, %s, %s,%s)"
            else:
                sql = "INSERT INTO customer ( firstname,lastname,gender,contact_number,username, email, password) VALUES (%s, %s, %s, %s, %s, %s,%s)"
            
            val = (firstname,lastname,gender,contact_number,username,email,password)
            
            
            mycursor.execute(sql, val)
            mydb.commit()


            if(type == "owner"):
                sql = "SELECT owner_id as id,firstname,lastname,gender,contact_number,username,email from owner where username=%s"
            else:
                sql = "SELECT user_id as id,firstname,lastname,gender,contact_number,username,email from customer where username=%s"
        

            
            mycursor.execute(sql, [username])
            myresult = mycursor.fetchall()
            
            mydb.commit()
            print(myresult)
            for id,firstname,lastname,gender,contact_number,username,email in myresult:
                user = User(id,firstname,lastname,gender,contact_number,username,email,type)
            print user.toJSON()
            session['user'] = vars(user)
            return redirect(url_for('home_blueprint.home'))
        except mysql.connector.Error as err:
            print(err)
    elif request.method == 'POST':
        return render_template('registration.html', form=form,error=True)

    return render_template('registration.html', form=form,)