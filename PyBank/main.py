import os
import csv

# absolute_path = "C:\Users\e.a.wright\OneDrive\Desktop\python-challenge\PyBank\Resources\budget_data.csv"
# relative_path = "PyBank\Resources\budget_data.csv"

file_path = os.path.join("Resources", "budget_data.csv")

with open(file_path,newline='') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

