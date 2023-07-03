from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': '001',
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000/-'
  },
  {
    'id': '002',
    'title': 'Business Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 13,000,000/-'
  },
  {
    'id': '003',
    'title': 'Data Scientist',
    'location': 'Mumbai, India',
    'salary': 'Rs. 2,000,000/-'
  },
  {
    'id': '004',
    'title': 'Financial Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 4,000,000/-'
  },
  {
    'id': '005',
    'title': 'Marketing Analyst',
    'location': 'Pune, India',
    'salary': 'Rs. 5,000,000/-'
  },
  {
    'id': '006',
    'title': 'Backend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 5,000,000/-'
  },
  {
    'id': '007',
    'title': 'Python developer',
    'location': 'Pune, India',
    'salary': 'Rs. 4,000,000'
  },
]


@app.route("/")
def hellojovian():
  return render_template('home.html', jobs=JOBS, company_name="Jovian")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
