import sqlalchemy
import csv

db = sqlalchemy.create_engine('mysql+pymysql://root:copper@localhost/Game_Square')

def insert_games():
    # Create tables (if they don't already exist)
	with db.connect() as conn:
		print('started')
		with open('Final_All_Games.csv') as file:
			csv_reader = csv.reader(file, delimiter=',')
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

def insert_exclusives():
	# Create tables (if they don't already exist)
	with db.connect() as conn:
		print('started')
		with open('Exclusive_Games') as file:
			csv_reader = csv.reader(file, delimiter=',')
			for row in csv_reader:
				try:
					conn.execute(
						"INSERT INTO Exclusive_Games(title, link, platform)"
						"VALUES ('" + row[0] + "', '" + row[1] + "', '" + row[2] + "');"
					)
					print('inserted ' + row[0] + '\n')
				except:
					print('skip')

def insert_ps3():
	# Create tables (if they don't already exist)
	with db.connect() as conn:
		print('started')
		with open('PS3_Games') as file:
			csv_reader = csv.reader(file, delimiter=',')
			for row in csv_reader:
				try:
					conn.execute(
						"INSERT INTO PS3_Games(title, link)"
						"VALUES ('" + row[0] + "', '" + row[1] + "');"
					)
					print('inserted ' + row[0] + '\n')
				except:
					print('skip')

def insert_ps4():
	# Create tables (if they don't already exist)
	with db.connect() as conn:
		print('started')
		with open('PS4_Games') as file:
			csv_reader = csv.reader(file, delimiter=',')
			for row in csv_reader:
				try:
					conn.execute(
						"INSERT INTO PS4_Games(title, link)"
						"VALUES ('" + row[0] + "', '" + row[1] + "');"
					)
					print('inserted ' + row[0] + '\n')
				except:
					print('skip')

def insert_xboxone():
	# Create tables (if they don't already exist)
	with db.connect() as conn:
		print('started')
		with open('XboxOne_Games') as file:
			csv_reader = csv.reader(file, delimiter=',')
			for row in csv_reader:
				try:
					conn.execute(
						"INSERT INTO XboxOne_Games(title, link)"
						"VALUES ('" + row[0] + "', '" + row[1] + "');"
					)
					print('inserted ' + row[0] + '\n')
				except:
					print('skip')

def insert_xbox360():
	# Create tables (if they don't already exist)
	with db.connect() as conn:
		print('started')
		with open('Xbox360_Games') as file:
			csv_reader = csv.reader(file, delimiter=',')
			for row in csv_reader:
				try:
					conn.execute(
						"INSERT INTO Xbox360_Games(title, link)"
						"VALUES ('" + row[0] + "', '" + row[1] + "');"
					)
					print('inserted ' + row[0] + '\n')
				except:
					print('skip')

def insert_wiiu():
	# Create tables (if they don't already exist)
	with db.connect() as conn:
		print('started')
		with open('WiiU_Games') as file:
			csv_reader = csv.reader(file, delimiter=',')
			for row in csv_reader:
				try:
					conn.execute(
						"INSERT INTO WiiU_Games(title, link)"
						"VALUES ('" + row[0] + "', '" + row[1] + "');"
					)
					print('inserted ' + row[0] + '\n')
				except:
					print('skip')

def insert_switch():
	# Create tables (if they don't already exist)
	with db.connect() as conn:
		print('started')
		with open('Switch_Games') as file:
			csv_reader = csv.reader(file, delimiter=',')
			for row in csv_reader:
				try:
					conn.execute(
						"INSERT INTO Switch_Games(title, link)"
						"VALUES ('" + row[0] + "', '" + row[1] + "');"
					)
					print('inserted ' + row[0] + '\n')
				except:
					print('skip')

if __name__ == '__main__':
    #insert_games()
	insert_exclusives()
	insert_ps3()
	insert_ps4()
	insert_xboxone()
	insert_xbox360()
	insert_wiiu()
	insert_switch()
	print('function complete')