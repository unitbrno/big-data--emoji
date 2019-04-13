import csv

months = {"Jan": "01","Feb": "02","Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}

def clean(file_name):
    with open("fwdata.csv", mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(["time", "SRC", "DST", "PROTO", "SPT", "DPT"])
        file = open(file_name, "r")

        for line in file:
            try:
                line = line.split(' ')
                row = [months[line[0]] + '-' + '-'.join(line[1:3]), line[8][4:], line[9][4:]]
                if line[16][:5] == "PROTO":
                    row.append(line[16][6:])
                    row.append(line[17][4:])
                    row.append(line[18][4:])
                else:
                    row.append(line[15][6:])
                    row.append(line[16][4:])
                    row.append(line[17][4:])
                writer.writerow(row)
            except:
                print("done")
        
clean("ufw_short.log")

