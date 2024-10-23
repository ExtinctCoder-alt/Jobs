from flask import Flask, request ,render_template

app = Flask(__name__)

JOBS = [
  {'job_name': 'Data Analyst', 'location': 'Bangalore', 'salary': '1250000 INR'},
  {'job_name': 'Data Analyst', 'location': 'Remote', 'salary': '60000 GBP'},
  {'job_name': 'Front-end Developer', 'location': 'Delhi', 'salary': '1600000 INR'},
  {'job_name': 'SDE - 3', 'location': 'Mumbai', 'salary': '1050000 INR'},
  {'job_name': 'SDE - 3', 'location': 'Remote', 'salary': '90000 USD'},
  {'job_name': 'HR', 'location': 'Remote', 'salary': '7000000 INR'},
  {'job_name': 'Software Engineer', 'location': 'Bangalore', 'salary': '950000 INR'},
  {'job_name': 'Software Engineer', 'location': 'Remote', 'salary': '7000000 INR'},
  {'job_name': 'DevOps Engineer', 'location': 'Pune', 'salary': '1200000 INR'},
  {'job_name': 'DevOps Engineer', 'location': 'Remote', 'salary': '1300000 INR'},
  {'job_name': 'Full Stack Developer', 'location': 'Chennai', 'salary': '3800000 INR'},
  {'job_name': 'Backend Developer', 'location': 'Mumbai', 'salary': '800000 INR'},
  {'job_name': 'Frontend Developer', 'location': 'Delhi', 'salary': '1400000 INR'},
  {'job_name': 'QA Engineer', 'location': 'Bangalore', 'salary': '1800000 INR'},
  {'job_name': 'Cloud Engineer', 'location': 'Hyderabad', 'salary': '1050000 INR'},
  {'job_name': 'Machine Learning Engineer', 'location': 'Pune', 'salary': '70000 EUR'},
  {'job_name': 'Machine Learning Engineer', 'location': 'Remote', 'salary': '1100000 INR'},
  {'job_name': 'Mobile App Developer', 'location': 'Chennai', 'salary': '60000 GBP'},
  {'job_name': 'UI/UX Designer', 'location': 'Mumbai', 'salary': '70000 EUR'},
  {'job_name': 'Systems Analyst', 'location': 'Delhi', 'salary': '90000 USD'},
  {'job_name': 'Network Engineer', 'location': 'Bangalore', 'salary': '7000000 INR'},
  {'job_name': 'Technical Support Engineer', 'location': 'Hyderabad', 'salary': '900000 INR'},
  {'job_name': 'Database Administrator', 'location': 'Pune', 'salary': '75000 USD'},
  {'job_name': 'Security Analyst', 'location': 'Chennai', 'salary': '70000 EUR'},
  {'job_name': 'Product Manager', 'location': 'Mumbai', 'salary': '80000 EUR'},
  {'job_name': 'Web Developer', 'location': 'Delhi', 'salary': '120000 USD'},
  {'job_name': 'Game Developer', 'location': 'Bangalore', 'salary': '1250000 INR'},
  {'job_name': 'Blockchain Developer', 'location': 'Hyderabad', 'salary': '1600000 INR'},
  {'job_name': 'Project Manager', 'location': 'Remote', 'salary': '1250000 INR'}
]


loc=[]
salary=[]
job_name=[]
for job in JOBS:
  loc.append(job['location'])
  salary.append(job['salary'])
  job_name.append(job['job_name'])
salary=list(set(salary))
locations=list(set(loc))
job_name=list(set(job_name))
salary.sort()

@app.route('/')
def loginpage():
  return render_template('home.html',log_status='Logout',jobs=JOBS,locations=locations,inlinetext='Are you an employer?')

@app.route("/filter/",methods=[ 'GET','POST'])
def home():
  category=request.form.get('category')
  if category=='location':
     return render_template("afterhome.html",jobs=JOBS,log_status='Logout',inlinetext='Are you an employer?',categorylist=locations)
  elif category=='job_name':
     return render_template("afterhome.html",jobs=JOBS,log_status='Logout',inlinetext='Are you an employer?',categorylist=job_name)
  elif category =='salary':
    return render_template("afterhome.html",jobs=JOBS,log_status='Logout',inlinetext='Are you an employer?',categorylist=salary)
  else:
    return render_template("jobs.html",jobs=JOBS,log_status='Logout',inlinetext='Are you an employer?',categorylist=JOBS)


@app.route('/jobs/',methods=['get','post'])
def jobs():
    final=request.form.get('category2')
    if final in locations:
      x='location'
    elif final in job_name:
      x='job_name'
    elif final in salary:
      x='salary'
    else:
      x='all'
    return render_template("jobs.html",jobs=JOBS,log_status='Logout',inlinetext='Are you an employer?',x=x,y=final)

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