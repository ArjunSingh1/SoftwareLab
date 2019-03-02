#import flask framework
from flask import Flask, render_template, url_for
#import api request for github
from HttpHandler import get_contributors_statistics, get_issues_statistics

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

#hardcode=================================
@app.route("/consoles/console1")
def console1():
    return render_template('console1.html')

@app.route("/consoles/console2")
def console2():
    return render_template('console2.html')

@app.route("/consoles/console3")
def console3():
    return render_template('console3.html')

@app.route("/consoles/console4")
def console4():
    return render_template('console4.html')

@app.route("/consoles/console5")
def console5():
    return render_template('console5.html')
#==========================================

#games page
@app.route("/games")
def games(): 
	return render_template('games.html')

#hardcode=================================
@app.route("/games/game1")
def game1():
    return render_template('game1.html')

@app.route("/games/game2")
def game2():
    return render_template('game2.html')

@app.route("/games/game3")
def game3():
    return render_template('game3.html')

@app.route("/games/game4")
def game4():
    return render_template('game4.html')

@app.route("/games/game5")
def game5():
    return render_template('game5.html')
#=========================================

#rating page
@app.route("/rating")
def rating(): 
	return render_template('rating.html')

#about page
@app.route("/about")
def about(): 
	data = get_contributors_statistics()
	stats = get_issues_statistics()
	return render_template('about.html', data=data, stats=stats)

@app.errorhandler(500)
def server_error(e):
    return 'An internal error occurred.', 500

if __name__ == '__main__':
	app.run(debug=True)