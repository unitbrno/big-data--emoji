import csv
import os

def find_reboots():
    with open("find_reboots_result.csv", mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(["message", "Id", "TimeCreated"])

        for root, dirs, files in os.walk('./'):
            for file in files:                
                if file.endswith('.csv') and file != "find_reboots_result.csv" and file != "fwdata.csv" and file.find("_security.csv") < 0:
                    with open(file) as csvfile:
                        readCSV = csv.reader(csvfile, delimiter=';')
                        for line in readCSV:
                            if "rebooted" in line[0]:
                                row = [line[0], line[1], line[16]]
                                writer.writerow(row)
    
find_reboots()

