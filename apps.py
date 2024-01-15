from flask import Flask, render_template, send_file,flash,redirect
from flask_login import login_user,login_required
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField



login_manager = LoginManager()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'key'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

login_manager.init_app(app)

login_manager.login_view = 'login'



class LoginForm(FlaskForm):
    name = StringField('Enter the Name')
    password = PasswordField('Enter the Password')
    submit = SubmitField('SUBMIT')


@login_manager.user_loader
def load_user(user_id):
    return UserData.query.get(user_id)

	

class UserData(db.Model,UserMixin):
    __tablename__ = 'userdata'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    hash_password = db.Column(db.String(128))

    def __init__(self,name,hash_password):
        self.name = name
        self.hash_password = generate_password_hash(hash_password)

    def check_password(self,password):
        return check_password_hash(self.hash_password,password)


#Adding the User and Password of the Challenge:


#Adding the User and Password of the Challenge:



@app.route('/')
def index():
	return render_template('index.html')





@app.route('/ctf')
@login_required
def ctf():
	return render_template('thepageyoulookingfor.html')


@app.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = UserData.query.filter_by(name = form.name.data).first()

		if user != UserData.query.filter_by(name='ethan').first():
			flash('You Have Entered an Incorrect Username or Password, Please try again')
			return redirect('login')

		if user.check_password(form.password.data):
			login_user(user)
			return redirect('ctf')
		else:
			flash('You Have Entered an Incorrect Username or Password, Please try again')
			return redirect('login')
		
	return render_template('login.html',form=form)



# Create index function for upload and return files

@app.route('/Picture1View')
def Picture1View():
	return render_template('Picture1View.html')	

@app.route('/Picture2View')
def Picture2View():
	return render_template('Picture2View.html')	

@app.route('/Picture3View')
def Picture3View():
	return render_template('Picture3View.html')	

@app.route('/Picture4View')
def Picture4View():
	return render_template('Picture4View.html')	

@app.route('/Picture5View')
def Picture5View():
	return render_template('Picture5View.html')	

@app.route('/Picture1')
def Picture1():
	pic = "static/Picture1.png"
	return send_file(pic,as_attachment=True)	

@app.route('/Picture2')
def Picture2():
	pic = "static/Picture2.png"
	return send_file(pic,as_attachment=True)	

@app.route('/Picture3')
def Picture3():
	pic = "static/Picture3.png"
	return send_file(pic,as_attachment=True)	

@app.route('/Picture4')
def Picture4():
	pic = "static/Picture4.png"
	return send_file(pic,as_attachment=True)	

@app.route('/Picture5')
def Picture5():
	pic = "static/Picture5.png"
	return send_file(pic,as_attachment=True)	

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=int("3000"))