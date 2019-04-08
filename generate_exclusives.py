import csv
#{key : [title, platform]}

dict = {}
col1 = "title"
col2 = "platform"
def main():
    with open('All_Games') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if len(row) == 3:
                if row[1] != "unreleased":
                    dict[row[0]] = row[2]
        put_dictionary_in_csv()
        print("Done")


def put_dictionary_in_csv():
    with open('Exclusive_Games', mode='w') as file:
        write = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        write.writerow([col1,col2])
        for key, value in dict.items():
            write.writerow([key,value])


if __name__ == "__main__":
	main()



        