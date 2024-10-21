from flask import Flask, request ,render_template

app = Flask(__name__)

JOBS=[
  {'job_name':'Data Analyst','location':'Bengaluru'},
  {'job_name':'Front-end Developer','location':'Delhi','salary':'Rs. 70,00,000'},
  {'job_name':'SDE - 3','location':'Mumbai','salary':'Rs. 38,00,000'},
  {'job_name':'HR','location':'Remote','salary':'$ 120,000'}, 
  {"job_name": "Software Engineer", "location": "Bangalore", "salary": "hehe"},
  {"job_name": "Data Scientist", "location": "Hyderabad", "salary": "₹1,500,000"},
  {"job_name": "DevOps Engineer", "location": "Pune", "salary": "₹1,300,000"},
  {"job_name": "Full Stack Developer", "location": "Chennai", "salary": "₹1,100,000"},
  {"job_name": "Backend Developer", "location": "Mumbai", "salary": "₹1,250,000"},
  {"job_name": "Frontend Developer", "location": "Delhi", "salary": "₹1,150,000"},
  {"job_name": "QA Engineer", "location": "Bangalore", "salary": "₹1,000,000"},
  {"job_name": "Cloud Engineer", "location": "Hyderabad", "salary": "₹1,400,000"},
  {"job_name": "Machine Learning Engineer", "location": "Pune", "salary": "₹1,600,000"},
  {"job_name": "Mobile App Developer", "location": "Chennai"},
  {"job_name": "UI/UX Designer", "location": "Mumbai", "salary": "₹900,000"},
  {"job_name": "Systems Analyst", "location": "Delhi", "salary": "₹1,100,000"},
  {"job_name": "Network Engineer", "location": "Bangalore", "salary": "₹1,050,000"},
  {"job_name": "Technical Support Engineer", "location": "Hyderabad", "salary": "₹800,000"},
  {"job_name": "Database Administrator", "location": "Pune", "salary": "₹950,000"},
  {"job_name": "Security Analyst", "location": "Chennai", "salary": "₹1,100,000"},
  {"job_name": "Product Manager", "location": "Mumbai", "salary": "₹1,800,000"},
  {"job_name": "Web Developer", "location": "Delhi", "salary": "₹1,050,000"},
  {"job_name": "Game Developer", "location": "Bangalore"},
  {"job_name": "Blockchain Developer", "location": "Hyderabad", "salary": "Aukat ke bahar"},
  # Remote jobs
  {"job_name": "Remote Software Engineer", "location": "Remote", "salary": "$80,000"},
  {"job_name": "Remote Data Analyst", "location": "Remote", "salary": "€70,000"},
  {"job_name": "Remote Project Manager", "location": "Remote", "salary": "£60,000"},
  {"job_name": "Remote UX Designer", "location": "Remote", "salary": "$75,000"},
  {"job_name": "Remote Frontend Developer", "location": "Remote", "salary": "₹1,200,000"},
  {"job_name": "Remote DevOps Engineer", "location": "Remote", "salary": "€80,000"},
  {"job_name": "Remote QA Tester", "location": "Remote", "salary": "£50,000"},
  {"job_name": "Remote Data Scientist", "location": "Remote", "salary": "$90,000"},
]



loc=[]
for job in JOBS:
  loc.append(job['location'])
locations=list(set(loc))



@app.route('/')
def loginpage():
  return render_template('home.html',log_status='Logout',jobs=JOBS,locations=locations,inlinetext='Are you an employer?')

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