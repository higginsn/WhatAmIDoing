from flask import Flask
app = Flask(__name__)

@app.route("/helloworld")
def hello():
	return "Hello bitches!"

if __name__ == "__main__":
	app.run()