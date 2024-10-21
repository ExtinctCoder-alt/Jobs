from flask import Flask, request ,render_template

app = Flask(__name__)

JOBS=[
  {
    'id':1,
    'job_name':'Data Analyst',
    'location':'Bengaluru'
  },
  {
    'id':2,
    'job_name':'Front-end Developer',
    'location':'Delhi',
    'salary':'Rs. 70,00,000'
  },
  {
    'id':3,
    'job_name':'SDE - 3',
    'location':'Mumbai',
    'salary':'Rs. 38,00,000'
  },
  {
    'id':4,
    'job_name':'HR',
    'location':'Remote',
    'salary':'$ 120,000'
  } 
]

@app.route('/')
def loginpage():
  return render_template('home.html',log_status='Logout',jobs=JOBS,inlinetext='Are you an employer?')

@app.route("/jobs/",methods=[ 'GET','POST'])
def home():
  location=request.form.get('location')
  return render_template("jobs.html",jobs=JOBS,log_status='Logout',inlinetext='Are you an employer?',loc=location)

@app.route('/aboutus/')
def about_us():
  return render_template('about_us.html',log_status='Logout',inlinetext='Are you an employer?')

@app.route('/login/')
def login():
  return render_template('login.html',log_status='Sign Up',inlinetext='Are you an employer?')

@app.route('/signup/')
def signup():
  return render_template('signup.html',log_status='Login',inlinetext='Are you an employer?')

@app.route('/signup/employer/')
def signup_employer():
  return render_template('signup.html',log_status='Login',employer='As an Employer')

@app.route('/login/employer/')
def login_employer():
  return render_template('login.html',log_status='Sign Up',employer='As an Employer')

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)