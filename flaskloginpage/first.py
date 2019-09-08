from flask import Flask,render_template,redirect,request,url_for
import csv
app=Flask(__name__)
@app.route('/')
def home():
	return redirect(url_for('login'))
@app.route('/welcome')
def welcome():
	return render_template('welcome.html')	
@app.route('/login',methods=['GET','POST'])
def login():
	error=None
	if request.method =='POST':
		user_name=request.form['username']
		user_password=request.form['password']
		#return render_template('welcome.html')
		f = open("credentials.csv","r")
		for line in f:
			#details = line.split(",")
			user, passw = line.strip().split(",")
			print(user, passw)
			#print(line)
			print(user_name, user_password)
			#details = line.split(",")
			if user_name==user and user_password==passw:
				return redirect(url_for('welcome'))
		else:
			error ='The credentials are invalid . Please try again.'
	return render_template('login.html',error=error)
#if __name__ =='__main':
app.run()
