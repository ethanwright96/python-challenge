import os
import csv

# absolute_path = "C:\Users\e.a.wright\python-challenge\PyBank\Resources\budget_data.csv"
# relative_path = "PyBank\Resources\budget_data.csv"

#Name file path 
file_path = os.path.join("Resources", "budget_data.csv")

#Read in csv file using csv module
with open (file_path) as budget_data:
    csv_reader=csv.reader(budget_data,delimiter=",")
    next(csv_reader)
    
    #Create empty lists to later append with csv's data
    date = []
    profit_loss = []
    change = []

    #Write for loop to append empty lists of for date and profit_loss
    for row in csv_reader:
        date.append((row[0])) 
        profit_loss.append(int(row[1]))
        
#Calculate total months and total profit/losses
total_months = len(date) #86
total = sum(profit_loss)

#Write for loop to find monthly change in profit/losses (current observation - former observation) 
for i in range(0,86):
    if i == 0:
        change.append(0)
    else:
        change.append(profit_loss[i]-profit_loss[i-1])

#Create and calculate variables for average and extreme change
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

#Concatinate results into string
results = ("Financial Analysis:"
f"\nTotal Months: {total_months}"
f"\nTotal: ${total}"
f"\nAverage Change: ${average_change}"
f"\nGreatest Increase in Profits: {gi_date} (${greatest_increase})"
f"\nGreatest Decrease in Profits: {gd_date} (${greatest_decrease})")

print(results)

#Write results into .txt file, joining path to analysis folder
with open (os.path.join("analysis","financial_analysis.txt"), 'w') as file:
    file.write(results)
    file.close()
    pass

