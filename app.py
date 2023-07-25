from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello, World"
# input url in the ""

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug=True)
  # host = '0.0.0.0' means this app is running locally
  # what if i want to run it on an online server?
