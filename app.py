from flask import Flask, render_template, jsonify

app = Flask(__name__)

LISTINGS =[
  {
  'id': 1,
  'title': 'bed frame',
  'location': 'Philadelphia',
  'price': '400',
  'email': 'email@gmail.com'
  },
  {
  'id': 2,
  'title': 'desk',
  'location': 'Philadelphia',
  'price': '150',
  'email': 'nothing'
  },
  {
  'id': 3,
  'title': 'office chair',
  #'location': 'Rodin'
  'price': '50'
  }
]
  

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         listings=LISTINGS)
# input url in the ""

@app.route("/api/listings")
def list_listings():
  return jsonify(LISTINGS)

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug=True)
  # host = '0.0.0.0' means this app is running locally
  # what if i want to run it on an online server?

