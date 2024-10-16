from flask import Flask, render_template

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
  return render_template('home.html',log_status='Logout',jobs=JOBS)

@app.route("/jobs/")
def home():
  return render_template("jobs.html",jobs=JOBS,log_status='Logout')

@app.route('/aboutus/')
def about_us():
  return render_template('about_us.html',log_status='Logout')

@app.route('/login/')
def login():
  return render_template('login.html',log_status='Sign Up')

@app.route('/signup/')
def signup():
  return render_template('signup.html',log_status='Login')

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)