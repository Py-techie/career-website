from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [{
    'id': '1',
    'Title': 'Data Analyst',
    'Experience': '3-8 Years',
    'Location': 'Bangalore',
    'Salary': 'Rs. 10,00,000'
}, {
    'id': '2',
    'Title': 'Data Scientist',
    'Experience': '5-10 Years',
    'Location': 'Pune',
    'Salary': 'Rs. 25,00,000'
}, {
    'id': '3',
    'Title': 'Frontend Developer',
    'Experience': '2-5 Years',
    'Location': 'Remote',
    'Salary': 'Rs. 12,50,000'
}, {
    'id': '4',
    'Title': 'Backend Developer',
    'Experience': '0-3 Years',
    'Location': 'Delhi',
    'Salary': 'Rs. 6,00,000'
}]


@app.route("/")
def home():
  return render_template("home.html", jobs=JOBS)

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
