from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def main():
	return render_template('Home.html')

@app.route("/about")
def about():
	return render_template('About.html')

if __name__ == '__name__':
	app.run(debug=True)