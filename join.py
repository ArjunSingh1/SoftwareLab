import csv

#{key : [title, link, platforms]}
dict = {}

def main():
	with open('PS4_Games', mode='r', newline='\n', encoding="utf-8") as PS4_file:
		add_to_dictionary(file=PS4_file, platform='PS4')
	with open('PS3_Games', mode='r', newline='\n', encoding="utf-8") as PS3_file:
		add_to_dictionary(file=PS3_file, platform='PS3')
	with open('Switch_Games', mode='r', newline='\n', encoding="utf-8") as Switch_file:
		add_to_dictionary(file=Switch_file, platform='Switch')
	with open('WiiU_Games', mode='r', newline='\n', encoding="utf-8") as Wii_file:
		add_to_dictionary(file=Wii_file, platform='WiiU')
	with open('Xbox360_Games', mode='r', newline='\n', encoding="utf-8") as Xbox360_file:
		add_to_dictionary(file=Xbox360_file, platform='Xbox360')
	with open('XboxOne_Games', mode='r', newline='\n', encoding="utf-8") as XboxOne_file:
		add_to_dictionary(file=XboxOne_file, platform='XboxOne')

	put_dictionary_in_csv()
	print("Done")



def add_to_dictionary(file,platform):
	readFile = csv.reader(file, delimiter=',')
	for row in readFile:
		if row[0] in dict.keys():
			platforms = dict[row[0]][2] + ',' + platform
			dict[row[0]][2] = platforms
		else:
			entry = []
			entry.append(row[0])
			if row[1]:
				entry.append(row[1])
			else:
				entry.append(None)
			entry.append(platform)
			dict[row[0]] = entry

def put_dictionary_in_csv():
	with open('All_Games', mode='w') as file:
		write = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE, escapechar ='\\', lineterminator='\n')
		for key, value in dict.items():
			write.writerow(value)


if __name__ == "__main__":
	main()

