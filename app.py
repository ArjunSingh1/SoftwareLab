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

@app.route("/games")
def games():
    return render_template('games.html')

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

@app.route("/about")
def about():
    stats = get_issues_statistics()
    data = get_contributors_statistics()
    return render_template('about.html', data=data, stats=stats)

@app.route("/rating")
def rating():
    return render_template('rating.html')

if __name__ == '__main__':
    app.run(debug=True)
