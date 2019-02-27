#import flask framework
from flask import Flask, render_template, url_for
#import api request for github
from HttpHandler import get_contributer_statistics

app = Flask(__name__)

#home page
@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

#consoles page
@app.route("/consoles")
def consoles(): 
	return render_template('consoles.html')

#games page
@app.route("/games")
def games(): 
	return render_template('games.html')

#rating page
@app.route("/rating")
def rating(): 
	return render_template('rating.html')

#about page
@app.route("/about")
def about(): 
	data = get_contributer_statistics()
	return render_template('about.html', data=data)

if __name__ == '__main__':
	app.run(debug=True)