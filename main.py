import datetime
import os
import logging
import csv
import random
from time import sleep
from forms import GameSearchForm
# from tables import Results

# import flask framework
from flask import Flask, render_template, url_for, request, Response, flash, redirect
# import api request for github
from HttpHandler import get_contributors_statistics, get_issues_statistics
# for databse connection
import sqlalchemy

# Remember - storing secrets in plaintext is potentially unsafe. Consider using
# something like https://cloud.google.com/kms/ to help keep secrets secret.
db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
db_name = os.environ.get("DB_NAME")
cloud_sql_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")

app = Flask(__name__)

# [START cloud_sql_mysql_sqlalchemy_create]
# The SQLAlchemy engine will help manage interactions, including automatically
# managing a pool of connections to your database
db = sqlalchemy.create_engine(
    # Equivalent URL:
    # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=/cloudsql/<cloud_sql_instance_name>
    sqlalchemy.engine.url.URL(
        drivername='mysql+pymysql',
        username=db_user,
        password=db_pass,
        database=db_name,
        query={
            'unix_socket': '/cloudsql/{}'.format(cloud_sql_connection_name)
        }
    ),
    pool_size=5,
    max_overflow=2,
    pool_timeout=30,  # 30 seconds
    pool_recycle=1800,  # 30 minutes
)


# db = sqlalchemy.create_engine('mysql+pymysql://root:copper@localhost/Game_Square')

# home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


# console pages
console1 = []
console2 = []
console3 = []
console4 = []
console5 = []
console6 = []

@app.route("/consoles")
def consoles():
    with db.connect() as conn:
        if sortmethod == 'All_Consoles':
            console1 = conn.execute(
                "SELECT * from All_Consoles WHERE console = 'XBOX ONE X'"
            ).fetchall()

            print(console1+'\n')

            console2 = conn.execute(
                "SELECT * from All_Consoles WHERE console = 'XBOX 360'"
            ).fetchall()

            print(console2 + '\n')

            console3 = conn.execute(
                "SELECT * from All_Consoles WHERE console = 'Switch'"
            ).fetchall()

            print(console3 + '\n')

            console4 = conn.execute(
                "SELECT * from All_Consoles WHERE console = 'PS4 Pro'"
            ).fetchall()

            print(console4 + '\n')

            console5 = conn.execute(
                "SELECT * from All_Consoles WHERE console = 'PS4 Slim'"
            ).fetchall()

            print(console5 + '\n')

            console6 = conn.execute(
                "SELECT * from All_Consoles WHERE console = 'Wii U'"
            ).fetchall()

            print(console6 + '\n')


    return render_template('consoles.html')


@app.route("/consoles/console1")
def console1():
    data = console1

    return render_template('console1.html', data=data)


@app.route("/consoles/console2")
def console2():
    data2 = console2
    return render_template('console2.html', data=data2)


@app.route("/consoles/console3")
def console3():
    data3 = console3

    return render_template('console3.html', data=data3)


@app.route("/consoles/console4")
def console4():
    data4 = console4

    return render_template('console4.html', data=data4)


@app.route("/consoles/console5")
def console5():
    data5 = console5

    return render_template('console5.html', data=data5)


@app.route("/consoles/console6")
def console6():
    data6 = console6

    return render_template('console6.html', data=data6)


@app.route("/consoles/compare")
def compare():
    overalldata = []
    with db.connect() as conn:
        if sortmethod == 'Comparison':
            data1= conn.execute(
                "SELECT CPU_,GPU,Memory_,Storage_,Mass,AV from Comparison WHERE console = 'XBOX ONE X'"
            ).fetchall()

            data2 = conn.execute(
                "SELECT CPU_,GPU,Memory_,Storage_,Mass,AV from Comparison WHERE console = 'XBOX 360'"
            ).fetchall()

            data3 = conn.execute(
                "SELECT CPU_,GPU,Memory_,Storage_,Mass,AV from Comparison WHERE console = 'Switch'"
            ).fetchall()

            data4 = conn.execute(
                "SELECT CPU_,GPU,Memory_,Storage_,Mass,AV from Comparison WHERE console = 'PS4 Pro'"
            ).fetchall()

            data5 = conn.execute(
                "SELECT CPU_,GPU,Memory_,Storage_,Mass,AV from Comparison WHERE console = 'PS4 Slim'"
            ).fetchall()

            data6 = conn.execute(
                "SELECT CPU_,GPU,Memory_,Storage_,Mass,AV from Comparison WHERE console = 'Wii U'"
            ).fetchall()

            overalldata.append(data1)
            print(overalldata + '\n')
            overalldata.append(data2)
            print(overalldata + '\n')
            overalldata.append(data3)
            print(overalldata + '\n')
            overalldata.append(data4)
            print(overalldata + '\n')
            overalldata.append(data5)
            print(overalldata + '\n')
            overalldata.append(data6)
            print(overalldata + '\n')

    return render_template('compare.html', data=overalldata)


# implementing games searching and sorting
@app.route('/index', methods=['GET', 'POST'])
def index():
    search = GameSearchForm(request.form)
    submit_type = 'search'
    if request.method == 'POST':
        return search_results(search, submit_type)
 
    return render_template('index.html', form=search)


@app.route('/results')
def search_results(search, submit_type):
    if submit_type == 'filter':
        search_string = ''
        if search.data['select'] == 'All_Games':
            sortmethod = 'All_Games'
        elif search.data['select'] == 'Exclusive_Games':
            sortmethod = 'Exclusive_Games'
        elif search.data['select'] == 'PS4_Games':
            sortmethod = 'PS4_Games'
        elif search.data['select'] == 'PS3_Games':
            sortmethod = 'PS3_Games'
        elif search.data['select'] == 'XboxOne_Games':
            sortmethod = 'XboxOne_Games'
        elif search.data['select'] == 'Xbox360_Games':
            sortmethod = 'Xbox360_Games'
        elif search.data['select'] == 'WiiU_Games':
            sortmethod = 'WiiU_Games'
        elif search.data['select'] == 'Switch_Games':
            sortmethod = 'Switch_Games'
        else:
            sortmethod = 'All_Games'
    else:
        search_string = search.data['search']
        sortmethod = ''
    
    return games(0, sortmethod, search_string)

@app.route('/filter', methods=['GET','POST'])
def filter():
    search = GameSearchForm(request.form)
    submit_type = 'filter'

    return search_results(search,submit_type)


# games page
@app.route("/games", methods=['GET', 'POST'], defaults={'page': 0})
def games(page, sortmethod, searchstring):
    perpage = 50
    startat = page * perpage
    games = []
    noimagerows = []
    # sqlstatement = "SELECT * from All_Games WHERE title like "
    with db.connect() as conn:
        if sortmethod == 'All_Games':
            top_games = conn.execute(
                "SELECT title, link, score, platform_one, platform_two, platform_three, platform_four, platform_five, platform_six FROM All_Games "
                "LIMIT {}, {}".format(startat, perpage)
            ).fetchall()
            for row in top_games:
                link = row[1].decode('utf-8')
                if link == 'unreleased':
                    noimagerows.append(row)
                else:
                    games.append({
                        'title': row[0].decode('utf-8'),
                        'link': link,
                        'score': row[2],
                        'platform_one': row[3],
                        'platform_two': row[4],
                        'platform_three': row[5],
                        'platform_four': row[6],
                        'platform_five': row[7],
                        'platform_six': row[8],
                    })

            for row in noimagerows:
                link = row[1].decode('utf-8')
                if link == 'unreleased':
                    link = 'https://www.classicposters.com/images/nopicture.gif'
                games.append({
                    'title': row[0].decode('utf-8'),
                    'link': link,
                    'score': row[2],
                    'platform_one': row[3],
                    'platform_two': row[4],
                    'platform_three': row[5],
                    'platform_four': row[6],
                    'platform_five': row[7],
                    'platform_six': row[8],
                })
        elif sortmethod == 'Exclusive_Games':
            top_games = conn.execute(
                "SELECT title, link FROM Exclusive_Games "
                "LIMIT {}, {}".format(startat, perpage)
            ).fetchall()
            for row in top_games:
                link = row[1].decode('utf-8')
                if link == 'unreleased':
                    link = 'https://www.classicposters.com/images/nopicture.gif'
                games.append({
                    'title': row[0].decode('utf-8'),
                    'link': link
                })
        elif sortmethod == 'PS4_Games':
            top_games = conn.execute(
                "SELECT title, link FROM PS4_Games "
                "LIMIT {}, {}".format(startat, perpage)
            ).fetchall()
            for row in top_games:
                link = row[1].decode('utf-8')
                if link == 'unreleased':
                    link = 'https://www.classicposters.com/images/nopicture.gif'
                games.append({
                    'title': row[0].decode('utf-8'),
                    'link': link
                })
        elif sortmethod == 'PS3_Games':
            top_games = conn.execute(
                "SELECT title, link FROM PS3_Games "
                "LIMIT {}, {}".format(startat, perpage)
            ).fetchall()
            for row in top_games:
                link = row[1].decode('utf-8')
                if link == 'unreleased':
                    link = 'https://www.classicposters.com/images/nopicture.gif'
                games.append({
                    'title': row[0].decode('utf-8'),
                    'link': link
                })
        elif sortmethod == 'XboxOne_Games':
            top_games = conn.execute(
                "SELECT title, link FROM XboxOne_Games "
                "LIMIT {}, {}".format(startat, perpage)
            ).fetchall()
            for row in top_games:
                link = row[1].decode('utf-8')
                if link == 'unreleased':
                    link = 'https://www.classicposters.com/images/nopicture.gif'
                games.append({
                    'title': row[0].decode('utf-8'),
                    'link': link
                })
        elif sortmethod == 'Xbox360_Games':
            top_games = conn.execute(
                "SELECT title, link FROM Xbox360_Games "
                "LIMIT {}, {}".format(startat, perpage)
            ).fetchall()
            for row in top_games:
                link = row[1].decode('utf-8')
                if link == 'unreleased':
                    link = 'https://www.classicposters.com/images/nopicture.gif'
                games.append({
                    'title': row[0].decode('utf-8'),
                    'link': link
                })
        elif sortmethod == 'WiiU_Games':
            top_games = conn.execute(
                "SELECT title, link FROM WiiU_Games "
                "LIMIT {}, {}".format(startat, perpage)
            ).fetchall()
            for row in top_games:
                link = row[1].decode('utf-8')
                if link == 'unreleased':
                    link = 'https://www.classicposters.com/images/nopicture.gif'
                games.append({
                    'title': row[0].decode('utf-8'),
                    'link': link
                })
        elif sortmethod == 'Switch_Games':
            top_games = conn.execute(
                "SELECT title, link FROM Switch_Games "
                "LIMIT {}, {}".format(startat, perpage)
            ).fetchall()
            for row in top_games:
                link = row[1].decode('utf-8')
                if link == 'unreleased':
                    link = 'https://www.classicposters.com/images/nopicture.gif'
                games.append({
                    'title': row[0].decode('utf-8'),
                    'link': link
                })
        else:
            rows = conn.execute(
                "SELECT * from Exclusive_Games WHERE title LIKE '%%{}%%'".format(searchstring)).fetchall()
            for row in rows:
                link = row[1].decode('utf-8')
                if link == 'unreleased':
                    link = 'https://www.classicposters.com/images/nopicture.gif'
                games.append({
                    'title': row[0].decode('utf-8'),
                    'link': link,
                    'score': row[2]
                })

    return render_template('games.html', games=games, page=page, sortmethod=sortmethod, searchstring=searchstring)


# handle Game page forward navigation
@app.route("/navigateNext", methods=['GET', 'POST'])
def navigateNext():
    page = request.form['page']
    sortmethod = request.form['sortmethod']
    searchstring = request.form['searchstring']

    if page != "600":
        page = int(page, 10) + 1

    return games(page, sortmethod, searchstring)


# handle Game page backward navigation
@app.route("/navigatePrevious", methods=['GET', 'POST'])
def navigatePrevious():
    page = request.form['page']
    sortmethod = request.form['sortmethod']
    searchstring = request.form['searchstring']
    if page != "0":
        page = int(page, 10) - 1
    return games(page, sortmethod, searchstring)


# easier SQL calls
class MySQL_Wrapper:
    def __init__(self, name=None, db=None, top=10):
        self.name = name
        self.db = db
        self.top = top
        if name is not None:
            import pandas as pd
            import numpy as np
            self.data = pd.read_csv(name)

    # Collects top x games from Scored_Games according to score
    def rank_games(self):
        games = []
        if (self.name is not None):
            data = self.data.sort_values('score', ascending=False).head(self.top)
            for i in range(data.shape[0]):
                games.append({
                    'title': data.iloc[i, 1],
                    'link': data.iloc[i, 2],
                    'score': data.iloc[i, data.shape[1] - 1]
                })
            return games

        with self.db.connect() as conn:
            # Execute the query and fetch all results
            top_games = conn.execute(
                "SELECT title, link, score FROM All_Games ORDER BY score DESC LIMIT {}".format(self.top)
            ).fetchall()

            for row in top_games:
                link = row[1].decode('utf-8')
                if link == 'unreleased':
                    link = 'https://www.classicposters.com/images/nopicture.gif'
                games.append({
                    'title': row[0].decode('utf-8'),
                    'link': link,
                    'score': row[2]
                })
        return games


# rating page
@app.route("/rating")
def rating():
    ranks = MySQL_Wrapper(db=db, top=10)
    top_games = ranks.rank_games()
    return render_template('rating.html', games=top_games)


# about page
@app.route("/about")
def about():
    data = get_contributors_statistics()
    sleep(0.1)
    stats = get_issues_statistics()  # stats = {'blake':0, 'wenran':0, 'yinghong':0, 'rabia':0, 'arjun':0, 'total': 0}
    return render_template('about.html', data=data, stats=stats)


# errors
@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    app.run(debug=True)