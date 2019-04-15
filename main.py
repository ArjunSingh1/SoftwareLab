import datetime
import os
import logging
import csv
from time import sleep

#import flask framework
from flask import Flask, render_template, url_for, request, Response
#import api request for github
from HttpHandler import get_contributors_statistics, get_issues_statistics
#for databse connection
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
    # ... Specify additional properties here.
    # [START_EXCLUDE]

    # [START cloud_sql_mysql_sqlalchemy_limit]
    # Pool size is the maximum number of permanent connections to keep.
    pool_size=5,
    # Temporarily exceeds the set pool_size if no connections are available.
    max_overflow=2,
    # The total number of concurrent connections for your application will be
    # a total of pool_size and max_overflow.
    # [END cloud_sql_mysql_sqlalchemy_limit]

    # [START cloud_sql_mysql_sqlalchemy_backoff]
    # SQLAlchemy automatically uses delays between failed connection attempts,
    # but provides no arguments for configuration.
    # [END cloud_sql_mysql_sqlalchemy_backoff]

    # [START cloud_sql_mysql_sqlalchemy_timeout]
    # 'pool_timeout' is the maximum number of seconds to wait when retrieving a
    # new connection from the pool. After the specified amount of time, an
    # exception will be thrown.
    pool_timeout=30,  # 30 seconds
    # [END cloud_sql_mysql_sqlalchemy_timeout]

    # [START cloud_sql_mysql_sqlalchemy_lifetime]
    # 'pool_recycle' is the maximum number of seconds a connection can persist.
    # Connections that live longer than the specified amount of time will be
    # reestablished
    pool_recycle=1800,  # 30 minutes
    # [END cloud_sql_mysql_sqlalchemy_lifetime]

    # [END_EXCLUDE]
)
# [END cloud_sql_mysql_sqlalchemy_create]

#home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

# consoles page
@app.route("/consoles")
def consoles():
    return render_template('consoles.html')

@app.route("/consoles/console1")
def console1():
    data = []
    with open('data/consoles.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data.append("".join(row))
    return render_template('console1.html', data=data)

@app.route("/consoles/console2")
def console2():
    data2 = []
    with open('data/consoles5.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data2.append("".join(row).strip())
    return render_template('console2.html', data=data2)

@app.route("/consoles/console3")
def console3():
    data3 = []
    with open('data/consoles2.csv','rU') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data3.append("".join(row).strip())
    return render_template('console3.html', data=data3)

@app.route("/consoles/console4")
def console4():
    data4 = []
    with open('data/consoles4.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data4.append("".join(row).strip())
    return render_template('console4.html', data=data4)

@app.route("/consoles/console5")
def console5():
    data5 = []
    with open('data/consoles3.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data5.append("".join(row).strip())
    return render_template('console5.html', data=data5)

@app.route("/consoles/console6")
def console6():
    data6 = []
    with open('data/consoles6.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data6.append("".join(row))
    return render_template('console6.html', data=data6)

@app.route("/consoles/compare")
def compare():
    return render_template('compare.html')

#games page
#@app.route("/games")
#def games(): 

 #   games = []
  #  with db.connect() as conn:
   #     # Execute the query and fetch all results
    #    top_games = conn.execute(
     #       "SELECT title, link FROM All_Games "
      #      "LIMIT 50;"
       # ).fetchall()
        # Convert the results into a list of dicts representing votes
        #for row in top_games:
         #   if row[1] == 'unreleased':
          #      row[1] = 'https://www.classicposters.com/images/nopicture.gif'
           # games.append({
            #    'title': row[0],
             #   'link': row[1]
            #})

    #return render_template('games.html', games=games)

@app.route('/games', defaults={'page':1})
@app.route('/games/page/<int:page>')
def games(page):
    games = []
    perpage = 100
    startat=page*perpage
    with db.connect() as cursor:
        top_games = cursor.execute('SELECT title,link FROM All_Games limit 20 offset 0;', (startat, perpage)).fetchall()
    for row in top_games:
        if row[1] == 'unreleased':
            row[1] = 'https://www.classicposters.com/images/nopicture.gif'
            games.append({
                'title' : row[0],
                'link' : row[1]
            })

    return render_template('games.html', games=games)


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


#rating page
@app.route("/rating")
def rating(): 
	return render_template('rating.html')

#about page
@app.route("/about")
def about():
    data = get_contributors_statistics()
    sleep(0.1)
    stats = get_issues_statistics() #stats = {'blake':0, 'wenran':0, 'yinghong':0, 'rabia':0, 'arjun':0, 'total': 0}
    return render_template('about.html', data=data, stats=stats)

#errors
@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
	app.run(debug=True)
