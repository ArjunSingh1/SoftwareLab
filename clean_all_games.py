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
    with open('games_lists\latest_games_lists\All_Games.csv', mode='r', newline='\n') as games_file:
        clean_bad_lines(file=games_file)
    put_dictionary_in_csv()
    print("done")
    

def clean_bad_lines(file):
    readFile = csv.reader(file, delimiter=',')
    for row in readFile:
        if len(row) == 8:
            entry = []
            entry.append(row[0])
            entry.append(row[1])
            entry.append(row[2])
            entry.append(row[3])
            entry.append(row[4])
            entry.append(row[5])
            entry.append(row[6])
            entry.append(row[7])
            dict[row[0]] = entry
            



def put_dictionary_in_csv():
	with open('Final_All_Games.csv', mode='w', encoding='utf-8') as file:
		write = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE, escapechar ='\\', lineterminator='\n')
		write.writerow([col1,col2,col3,col4,col5,col6,col7,col8])
		for key, value in dict.items():
			write.writerow(value)
            
            
if __name__ == "__main__":
	main()