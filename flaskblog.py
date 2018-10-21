from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
	return "<h1>HomePage</h1>"

@app.route("/about")
def about():
	return "<h2>AboutPage</h2>"

if __name__ == "__main__":
	app.run(debug=True)
