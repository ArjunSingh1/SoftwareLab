from flask import Flask, render_template
from HttpHandler import get_issues_statistics, get_contributors_statistics
app = Flask(__name__)

@app.route("/")

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/consoles")
def consoles():
    return render_template('consoles.html')

@app.route("/games")
def games():
    return render_template('games.html')

@app.route("/about")
def about():
    stats = get_issues_statistics()
    data = get_contributors_statistics()
    return render_template('about.html', data=data, stats=stats)

@app.route("/rating")
def rating():
    return render_template('rating.html')

if __name__ == '__main__':
    app.run()
