import csv
#{key : [title, platform]}

dict = {}
col1 = 'title'
col2 = 'image_link'
col3 = 'platform'
def main():
    with open('games_lists/All_Games') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if len(row) == 3:
                if row[1] != "unreleased":
                    entry = []
                    entry.append(row[0])
                    entry.append(row[1])
                    entry.append(row[2])
                    dict[row[0]] = entry
        put_dictionary_in_csv()
        print("Done")


def put_dictionary_in_csv():
    with open('Exclusive_Games', mode='w') as file:
        write = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONE, escapechar='\\', lineterminator='\n')
        write.writerow([col1,col2,col3])
        for key, value in dict.items():
            write.writerow(value)


if __name__ == "__main__":
	main()



        