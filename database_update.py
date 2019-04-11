import sqlalchemy
import csv

db = sqlalchemy.create_engine('mysql+pymysql://root:copper@localhost/Game_Square')

def insert_games():
    # Create tables (if they don't already exist)
	with db.connect() as conn:
		print('started')
		with open('Final_All_Games.csv') as file:
			csv_reader = csv.reader(file, delimiter=',')
			line_count = 0
			for row in csv_reader:
				try:
					conn.execute(
						"INSERT INTO All_Games(title, link)"
						"VALUES ('" + row[0] + "', '" + row[1] + "');"
					)
					print('inserted ' + row[0] + '\n')
				except:
					print('skip')
	print('finished')

if __name__ == '__main__':
    insert_games()
    print('function complete')