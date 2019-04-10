import csv

#{key : [title, image_link, platforms]}
dict = {}
col1 = "title"
col2 = "image_link"
col3 = "platform1"
col4 = "platform2"
col5 = "platform3"
col6 = "platform4"
col7 = "platform5"
col8 = "platform6"
colNA = "na"

def main():
	with open('PS4_Games', mode='r', newline='\n') as PS4_file:
		add_to_dictionary(file=PS4_file, platform='PS4')
	with open('PS3_Games', mode='r', newline='\n') as PS3_file:
		add_to_dictionary(file=PS3_file, platform='PS3')
	with open('Switch_Games', mode='r', newline='\n') as Switch_file:
		add_to_dictionary(file=Switch_file, platform='Switch')
	with open('WiiU_Games', mode='r', newline='\n') as Wii_file:
		add_to_dictionary(file=Wii_file, platform='WiiU')
	with open('Xbox360_Games', mode='r', newline='\n') as Xbox360_file:
		add_to_dictionary(file=Xbox360_file, platform='Xbox360')
	with open('XboxOne_Games', mode='r', newline='\n') as XboxOne_file:
		add_to_dictionary(file=XboxOne_file, platform='XboxOne')

	fill_in_empty_cols()
	put_dictionary_in_csv()
	print("Done")



def add_to_dictionary(file,platform):
	readFile = csv.reader(file, delimiter=',')
	for row in readFile:
		if row[0] != "title":
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

def fill_in_empty_cols():
	for value in dict.values():
		platforms = value[2]
		rowlength = platforms.count(',') + 3
		for i in range(8-rowlength):
			value.append("na")

def put_dictionary_in_csv():
	with open('All_Games', mode='w') as file:
		write = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE, escapechar ='\\', lineterminator='\n')
		write.writerow([col1,col2,col3,col4,col5,col6,col7,col8])
		for key, value in dict.items():
			write.writerow(value)


if __name__ == "__main__":
	main()

