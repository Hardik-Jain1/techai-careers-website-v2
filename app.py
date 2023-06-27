from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': "Data Analyst",
  'location': "Bangluru, India",
  'salary': "Rs 10,000,000"
}, {
  'id': 2,
  'title': "Data Science",
  'location': "London, England",
  'salary': "£ 150,000"
}, {
  'id': 3,
  'title': "Machine Learning Engineer",
  'location': "San Francisco, USA",
  'salary': "$ 200,000"
}, {
  'id': 4,
  'title': "Backend Engineer",
  'location': "Paris, France"
}, {
  'id': 5,
  'title': "Artificial Intelligence Engineer",
  'location': "Zurich, Switzerland",
  'salary': "CHF 300,000"
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name='TechAI')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
