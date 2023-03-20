import os
import csv

# absolute_path = "C:\Users\e.a.wright\python-challenge\PyBank\Resources\budget_data.csv"
# relative_path = "PyBank\Resources\budget_data.csv"

file_path = os.path.join("Resources", "budget_data.csv")

with open(file_path) as budget_data:
    csv_reader=csv.reader(budget_data,delimiter=",")
    next(csv_reader)
    
    #Create empty lists to later append with csv's data
    date = []
    profit_loss = []
    change = []
    #Define function to calculate profit/losses change

    for row in csv_reader:
        #Add 'Date' to empty list "date"
        date.append((row[0])) #This does not work when row[0] is casted with str()
        #Add 'Profit/Losses', casted as integer, to empty list "profit_loss"
        profit_loss.append(int(row[1]))
        #Harvest changes in "Profit/Losses"

total_months = len(date) #86
total = sum(profit_loss)
#calculate average change

# For every iteration, take the difference between the current observation and the former observation 
# If the observation's index == 0, then the change value = NA

for i in range(0,86):
    if i == 0:
        change.append(0)
    else:
        change.append(profit_loss[i]-profit_loss[i-1])

average_change = round(sum(change)/(total_months-1),2)
greatest_increase = max(change)
greatest_decrease = min(change)

def find(lst,a,b):
    for x in lst:
        if x == a:
            i = lst.index(x)
            result = b[i]
    return result

gi_date = find(change,greatest_increase,date)
gd_date = find(change,greatest_decrease,date)

print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {gi_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {gd_date} (${greatest_decrease})")



# # Write a function that returns the arithmetic average for a list of numbers
# def average(numbers):
#     length = len(numbers)
#     total = 0.0
#     for number in numbers:
#         total += number
#     return total / length


# for x in range(1,86):
#     new.append(profit_loss[x]) 


    #   print(type(row)) #row in csv_reader is of the data type/class 'list'
    #   print(len(row)) #the length of each row in csv_reader is 2 ('Date' & 'Profit/Losses')


# Your task is to create a Python script that analyzes the records to calculate each of the following values:

# * The total number of months included in the dataset

# * The net total amount of "Profit/Losses" over the entire period

# * The changes in "Profit/Losses" over the entire period, and then the average of those changes

# * The greatest increase in profits (date and amount) over the entire period

# * The greatest decrease in profits (date and amount) over the entire period

# Your analysis should align with the following results:


# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)



# a = []
# bucket = [1,2,3,4,5]
# for i in bucket:
#    a.append(i)

# print(a)
# print(type(a))
