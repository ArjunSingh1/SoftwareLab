import sqlalchemy
import csv
import re

db = sqlalchemy.create_engine('mysql+pymysql://root:copper@localhost/Game_Square')

game_scores = {}

def get_scores():
	with open('Scored_Games.csv') as file:
		read = csv.reader(file, delimiter=',')
		for row in read:
			game_scores[row[0]] = row[1]

def insert_consoles():
    # Create tables (if they don't already exist)
	with db.connect() as conn:
		print('started consoles')
		with open('consoles.csv') as file:
			csv_reader = csv.reader(file, delimiter=',')
			for row in csv_reader:
				conn.execute(
					"INSERT INTO All_Consoles(Console,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15)"
					"VALUES ('" + row[0] + "', '" + row[1] + "', '" + row[2] + "', '" + row[3] + "', '" + row[4] + "', '" + row[5] + "', '" + row[6] + "', '" + row[7] + "', '" + row[8] + "', '" + row[9] + "', '" + row[10] + "', '" + row[11] + "', '" + row[12] + "', '" + row[13] + "', '" + row[14] + "', '" + row[15] + "');"
				)
				print('inserted ' + row[0] + '\n')

	print('finished')

def insert_comparison():
	# Create tables (if they don't already exist)
	with db.connect() as conn:
		print('started comp')
		with open('AllConsoles.csv') as file:
			csv_reader = csv.reader(file, delimiter=',')
			for row in csv_reader:
				conn.execute(
					"INSERT INTO Comparison(Console,CPU_,GPU,Memory_,Storage_,Mass,AV)"
					"VALUES ('" + row[0] + "', '" + row[1] + "', '" + row[2] + "', '" + row[3] + "', '" + row[4] + "', '" + row[5] + "', '" + row[6] + "');"
				)
				print('inserted ' + row[0] + '\n')
	print('finished')


def insert_games():
    # Create tables (if they don't already exist)
	with db.connect() as conn:
		print('started')
		with open('games_lists/latest_games_lists/All_Games.csv') as file:
			csv_reader = csv.reader(file, delimiter=',')
			for row in csv_reader:
				if game_scores.has_key(row[0]):
					score = game_scores[row[0]]
					try:
						conn.execute(
							"INSERT INTO All_Games(title, link, score, platform_one, platform_two, platform_three, platform_four, platform_five, platform_six)"
							"VALUES ('{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}');".format(row[0], row[1], score, re.escape(row[2]), re.escape(row[3]), re.escape(row[4]), re.escape(row[5]), re.escape(row[6]), re.escape(row[7]))
						)
						print('inserted ' + row[0] + ' to all\n')
					except:
						print('skip insert')
	print('finished')

def insert_exclusives():
	# Create tables (if they don't already exist)
	with db.connect() as conn:
		print('started')
		with open('games_lists/latest_games_lists/Exclusive_Games.csv') as file:
			csv_reader = csv.reader(file, delimiter=',')
			for row in csv_reader:
				if game_scores.has_key(row[0]):
					score = game_scores[row[0]]
					try:
						conn.execute(
							"INSERT INTO Exclusive_Games(title, link, score, platform)"
							"VALUES ('{}', '{}', {}, '{}');".format(row[0], row[1], score, row[2])
						)
						print('inserted ' + row[0] + ' to exclusive\n')
					except:
						print('skip')

def insert_ps3():
	# Create tables (if they don't already exist)
	with db.connect() as conn:
		print('started')
		with open('games_lists/latest_games_lists/PS3_Games.csv') as file:
			csv_reader = csv.reader(file, delimiter=',')
			for row in csv_reader:
				if game_scores.has_key(row[0]):
					score = game_scores[row[0]]
					try:
						conn.execute(
							"INSERT INTO PS3_Games(title, link, score)"
							"VALUES ('{}', '{}', {});".format(row[0], row[1], score)
						)
						print('inserted ' + row[0] + ' to PS3\n')
					except:
						print('skip')

def insert_ps4():
	# Create tables (if they don't already exist)
	with db.connect() as conn:
		print('started')
		with open('games_lists/latest_games_lists/PS4_Games.csv') as file:
			csv_reader = csv.reader(file, delimiter=',')
			for row in csv_reader:
				if game_scores.has_key(row[0]):
					score = game_scores[row[0]]
					try:
						conn.execute(
							"INSERT INTO PS4_Games(title, link, score)"
							"VALUES ('{}', '{}', {});".format(row[0], row[1], score)
						)
						print('inserted ' + row[0] + '\n')
					except:
						print('skip')

def insert_xboxone():
	# Create tables (if they don't already exist)
	with db.connect() as conn:
		print('started')
		with open('games_lists/latest_games_lists/XboxOne_Games.csv') as file:
			csv_reader = csv.reader(file, delimiter=',')
			for row in csv_reader:
				if game_scores.has_key(row[0]):
					score = game_scores[row[0]]
					try:
						conn.execute(
							"INSERT INTO XboxOne_Games(title, link, score)"
							"VALUES ('{}', '{}', {});".format(row[0], row[1], score)
						)
						print('inserted ' + row[0] + '\n')
					except:
						print('skip')

def insert_xbox360():
	# Create tables (if they don't already exist)
	with db.connect() as conn:
		print('started')
		with open('games_lists/latest_games_lists/Xbox360_Games.csv') as file:
			csv_reader = csv.reader(file, delimiter=',')
			for row in csv_reader:
				if game_scores.has_key(row[0]):
					score = game_scores[row[0]]
					try:
						conn.execute(
							"INSERT INTO Xbox360_Games(title, link, score)"
							"VALUES ('{}', '{}', {});".format(row[0], row[1], score)
						)
						print('inserted ' + row[0] + '\n')
					except:
						print('skip')

def insert_wiiu():
	# Create tables (if they don't already exist)
	with db.connect() as conn:
		print('started')
		with open('games_lists/latest_games_lists/WiiU_Games.csv') as file:
			csv_reader = csv.reader(file, delimiter=',')
			for row in csv_reader:
				if game_scores.has_key(row[0]):
					score = game_scores[row[0]]
					try:
						conn.execute(
							"INSERT INTO WiiU_Games(title, link, score)"
							"VALUES ('{}', '{}', {});".format(row[0], row[1], score)
						)
						print('inserted ' + row[0] + '\n')
					except:
						print('skip')

def insert_switch():
	# Create tables (if they don't already exist)
	with db.connect() as conn:
		print('started')
		with open('games_lists/latest_games_lists/Switch_Games.csv') as file:
			csv_reader = csv.reader(file, delimiter=',')
			for row in csv_reader:
				if game_scores.has_key(row[0]):
					score = game_scores[row[0]]
					try:
						conn.execute(
							"INSERT INTO Switch_Games(title, link, score)"
							"VALUES ('{}', '{}', {});".format(row[0], row[1], score)
						)
						print('inserted ' + row[0] + '\n')
					except:
						print('skip')

def clear_and_remake():
	with db.connect() as conn:
		try:
			conn.execute(
				"DROP TABLE IF EXISTS Switch_Games;"
			)
			conn.execute(
				"DROP TABLE IF EXISTS WiiU_Games;"
			)
			conn.execute(
				"DROP TABLE IF EXISTS PS3_Games;"
			)
			conn.execute(
				"DROP TABLE IF EXISTS PS4_Games;"
			)
			conn.execute(
				"DROP TABLE IF EXISTS All_Games;"
			)
			conn.execute(
				"DROP TABLE IF EXISTS Exclusive_Games;"
			)
			conn.execute(
				"DROP TABLE IF EXISTS Xbox360_Games;"
			)
			conn.execute(
				"DROP TABLE IF EXISTS XboxOne_Games;"
			)
			print('delete success')
		except:
			print('delete failed')
		try:
			conn.execute(
				"CREATE TABLE IF NOT EXISTS Exclusive_Games(title VARCHAR(75) NOT NULL, link VARCHAR(125), score DOUBLE, platform VARCHAR(25) NOT NULL);"
			)
			conn.execute(
				"CREATE TABLE IF NOT EXISTS Switch_Games(title VARCHAR(75) NOT NULL, link VARCHAR(125), score DOUBLE);"
			)
			conn.execute(
				"CREATE TABLE IF NOT EXISTS WiiU_Games(title VARCHAR(75) NOT NULL, link VARCHAR(125), score DOUBLE);"
			)
			conn.execute(
				"CREATE TABLE IF NOT EXISTS PS3_Games(title VARCHAR(75) NOT NULL, link VARCHAR(125), score DOUBLE);"
			)
			conn.execute(
				"CREATE TABLE IF NOT EXISTS PS4_Games(title VARCHAR(75) NOT NULL, link VARCHAR(125), score DOUBLE);"
			)
			conn.execute(
				"CREATE TABLE IF NOT EXISTS Xbox360_Games(title VARCHAR(75) NOT NULL, link VARCHAR(125), score DOUBLE);"
			)
			conn.execute(
				"CREATE TABLE IF NOT EXISTS XboxOne_Games(title VARCHAR(75) NOT NULL, link VARCHAR(125), score DOUBLE);"
			)
			conn.execute(
				"CREATE TABLE IF NOT EXISTS All_Games(title VARCHAR(75) NOT NULL, link VARCHAR(125), score DOUBLE);"
			)
			print('remade')
		except:
			print('failed remake')


if __name__ == '__main__':
	choice = raw_input('input clear or make:')
	if choice == 'clear':
		clear_and_remake()
		print('remake complete')
	elif choice == 'make':
		insert_consoles()
		insert_comparison()
		print('insert complete')
		#get_scores()
		#insert_games()
		#insert_exclusives()
		#insert_ps3()
		#insert_ps4()
		#insert_xboxone()
		#insert_xbox360()
		#insert_wiiu()
		#insert_switch()

