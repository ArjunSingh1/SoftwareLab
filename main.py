import datetime
import os
import logging
import csv
import random
from time import sleep
from forms import GameSearchForm
# from tables import Results

# import flask framework
# import flask framework
from flask import Flask, render_template, url_for, request, Response, flash, redirect
from flask_bootstrap import Bootstrap
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
Bootstrap(app)

# [START cloud_sql_mysql_sqlalchemy_create]
# The SQLAlchemy engine will help manage interactions, including automatically
# managing a pool of connections to your database
#db = sqlalchemy.create_engine(
    # Equivalent URL:
    # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=/cloudsql/<cloud_sql_instance_name>
#    sqlalchemy.engine.url.URL(
#        drivername='mysql+pymysql',
#        username=db_user,
#        password=db_pass,
#        database=db_name,
#        query={
#            'unix_socket': '/cloudsql/{}'.format(cloud_sql_connection_name)
#        }
#    ),
#    pool_size=5,
#    max_overflow=2,
#    pool_timeout=30,  # 30 seconds
#    pool_recycle=1800,  # 30 minutes
#)


db = sqlalchemy.create_engine('mysql+pymysql://root:copper@localhost/Game_Square')

# home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


# easier data parsing for console pages
class Console_Wrapper:

    _instance = None

    @staticmethod
    def getInstance():

        if Console_Wrapper._instance == None:
            Console_Wrapper()
        return Console_Wrapper._instance

    def __init__(self):

        if Console_Wrapper._instance != None:
            raise Exception("This class is a singleton!")
        else:
            Console_Wrapper._instance = self

        self.db = db
        self.console_1 = []
        self.console_2 = []
        self.console_3 = []
        self.console_4 = []
        self.console_5 = []
        self.console_6 = []


    def get_data(self):

        with db.connect() as conn:
            consoles = conn.execute(
                "SELECT * from All_Consoles"
            ).fetchall()
        i = 0
        for row in consoles:
            if i == 1:
                for j in range(1, 10):
                    self.console_1.append(row[j])

            if i == 2:
                for j in range(1, 13):
                    self.console_2.append(row[j])

            if i == 3:
                for j in range(1, 15):
                    self.console_3.append(row[j])

            if i == 4:
                for j in range(1, 12):
                    self.console_4.append(row[j])

            if i == 5:
                for j in range(1, 12):
                    self.console_5.append(row[j])

            if i == 6:
                for j in range(1, 13):
                    self.console_6.append(row[j])

            i = i + 1

    def get_1(self):
        return self.console_1

    def get_2(self):
        return self.console_2

    def get_3(self):
        return self.console_3

    def get_4(self):
        return self.console_4

    def get_5(self):
        return self.console_5

    def get_6(self):
        return self.console_6


#Singleton Design Pattern implemented

@app.route("/consoles")
def consoles():
    console_data = Console_Wrapper()
    console_data.get_data()

    return render_template('consoles.html')


@app.route("/consoles/console1")
def console1():
    data = Console_Wrapper.getInstance().get_1()

    return render_template('console1.html', data=data)


@app.route("/consoles/console2")
def console2():
    data2 = Console_Wrapper.getInstance().get_2()
    return render_template('console2.html', data=data2)


@app.route("/consoles/console3")
def console3():
    data3 = Console_Wrapper.getInstance().get_3()

    return render_template('console3.html', data=data3)


@app.route("/consoles/console4")
def console4():
    data4 = Console_Wrapper.getInstance().get_4()

    return render_template('console4.html', data=data4)


@app.route("/consoles/console5")
def console5():
    data5 = Console_Wrapper.getInstance().get_5()

    return render_template('console5.html', data=data5)


@app.route("/consoles/console6")
def console6():
    data6 = Console_Wrapper.getInstance().get_6()

    return render_template('console6.html', data=data6)



@app.route("/consoles/compare")
def compare():
    overalldata = []
    with db.connect() as conn:

        data = conn.execute(
            "SELECT * from Comparison"
        ).fetchall()

    i = 0
    for row in data:
        if i != 0:
            overalldata.append(row[1])
            overalldata.append(row[2])
            overalldata.append(row[3])
            overalldata.append(row[4])
            overalldata.append(row[5])
            overalldata.append(row[6])
        i = i + 1

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
    if submit_type == 'search':
        if search.data['select'] == 'All':
            sortmethod = 'All_Games'
        elif search.data['select'] == 'Exclusives':
            sortmethod = 'Exclusive_Games'
        elif search.data['select'] == 'PS4':
            sortmethod = 'PS4_Games'
        elif search.data['select'] == 'PS3':
            sortmethod = 'PS3_Games'
        elif search.data['select'] == 'Xbox One':
            sortmethod = 'XboxOne_Games'
        elif search.data['select'] == 'Xbox 360':
            sortmethod = 'Xbox360_Games'
        elif search.data['select'] == 'Wii U':
            sortmethod = 'WiiU_Games'
        elif search.data['select'] == 'Nintendo Switch':
            sortmethod = 'Switch_Games'
        elif search.data['select'] == 'Highest Rated':
            sortmethod = 'Highest Rated'
        elif search.data['select'] == 'Lowest Rated':
            sortmethod = 'Lowest Rated'
        else:
            sortmethod = 'All_Games'
    search_string = search.data['search']

    return games(0, sortmethod, search_string)


# games page
@app.route("/games", methods=['GET', 'POST'], defaults={'page': 0})
def games(page, sortmethod, searchstring):
    perpage = 50
    startat = page * perpage
    games = []
    noimagerows = []
    with db.connect() as conn:
        if (searchstring == ''):
            if (sortmethod == 'Highest Rated') or (sortmethod == 'Lowest Rated'):
                if (sortmethod == 'Highest Rated'):
                    order = 'DESC'
                else:
                    order = 'ASC'
                top_games = conn.execute(
                    "SELECT * FROM All_Games ORDER BY score {} LIMIT {}, {}".format(order, startat, perpage)
                ).fetchall()
            else:
                top_games = conn.execute(
                    "SELECT * FROM {} LIMIT {}, {}".format(sortmethod, startat, perpage)
                ).fetchall()
            if (sortmethod == 'All_Games'):
                for row in top_games:
                    link = row[1].decode('utf-8')
                    if link == 'unreleased':
                        noimagerows.append(row)
                    else:
                        append_games(row, link, games, sortmethod)

                for row in noimagerows:
                    link = row[1].decode('utf-8')
                    if link == 'unreleased':
                        link = 'https://www.classicposters.com/images/nopicture.gif'
                    append_games(row, link, games, sortmethod)

            else:
                for row in top_games:
                    link = row[1].decode('utf-8')
                    if link == 'unreleased':
                        link = 'https://www.classicposters.com/images/nopicture.gif'
                    append_games(row, link, games, sortmethod)

        else:
            if (sortmethod == 'Highest Rated') or (sortmethod == 'Lowest Rated'):
                sortmethod = 'All_Games'
            rows = conn.execute(
                "SELECT * from {} WHERE title LIKE '%%{}%%'".format(sortmethod, searchstring)).fetchall()
            for row in rows:
                link = row[1].decode('utf-8')
                if link == 'unreleased':
                    link = 'https://www.classicposters.com/images/nopicture.gif'
                append_games(row, link, games, sortmethod)

    return render_template('games.html', games=games, page=page, sortmethod=sortmethod, searchstring=searchstring)


def append_games(row, link, games, sortmethod):
    if (sortmethod == 'All_Games') or (sortmethod == 'Highest Rated') or (sortmethod == 'Lowest Rated'):
        games.append({
            'title': row[0].decode('utf-8'),
            'link': link,
            'score': row[2],
            'platform_one': row[3],
            'platform_two': row[4],
            'platform_three': row[5],
            'platform_four': row[6],
            'platform_five': row[7],
            'platform_six': row[8]
        })
    elif (sortmethod == 'Exclusive_Games'):
        games.append({
            'title': row[0].decode('utf-8'),
            'link': link,
            'score': row[2],
            'platform': row[3]
        })
    else:
        games.append({
            'title': row[0].decode('utf-8'),
            'link': link,
            'score': row[2]
        })


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
    ranks2 = MySQL_Wrapper(db=db, top=20)
    top_games2 = ranks2.rank_games()
    ranks3 = MySQL_Wrapper(db=db, top=30)
    top_games3 = ranks3.rank_games()
    ranks4 = MySQL_Wrapper(db=db, top=40)
    top_games4 = ranks4.rank_games()
    ranks5 = MySQL_Wrapper(db=db, top=50)
    top_games5 = ranks5.rank_games()
    return render_template('rating.html', games=top_games, games2=top_games2, games3=top_games3, games4=top_games4,
                           games5=top_games5)


# about page
@app.route("/about")
def about():
    # data = get_contributors_statistics()
    # sleep(0.1)
    # stats = get_issues_statistics() stats = {'blake':0, 'wenran':0, 'yinghong':0, 'rabia':0, 'arjun':0, 'total': 0}
    return render_template('about.html')


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