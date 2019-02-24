#import flask framework
from flask import Flask, render_template
#import api request for github
from HttpHandler import get_contributer_statistics

app = Flask(__name__)

#home page
@app.route("/")
@app.route("/home")
def main():
	return render_template('Home.html')

#about page
@app.route("/about")
def about(): 
	data = get_contributer_statistics()
	return render_template('About.html', data=data)

if __name__ == '__name__':
	app.run(debug=True)