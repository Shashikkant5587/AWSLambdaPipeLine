import csv
import os

csvFileToRead = "./Users/shashikantpathak/Downloads/user.csv"

with open(csvFileToRead, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)
