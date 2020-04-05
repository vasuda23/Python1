import pandas as pd
import os
import csv

df= os.path.join("","budget_data.csv")

profit =[]
revenue = []
date = []
changes = []

#Declare variable
count=0
total=0
change =0
avg_change=0


with open(df) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csvheader = next(csvreader)


    for row in csvreader:
        total = total + int((row[1]))
        count=count + 1
        revenue.append(row[1])
        date.append(row[0])



    for i in (range(count-1)):
        delta = int(revenue[i+1]) - int(revenue[i])
        change += delta
        changes.append(delta)

    min_index= changes.index(max(changes))+1
    max_index= changes.index(min(changes))+1



    print("Total Month :"+str(count))
    print("Total : $" + str(total))
    print("Average Change: $" + str(round(change/(count-1),2)))
    print("Greatest Increase in Profits:"+ str(date[min_index]) + " ( $ " + str(max(changes)) + ")")
    print("Greatest Decrease in Profits:"+ str(date[max_index])  + " ( $ " + str(min(changes)) + ")")

    poll_output = os.path.join("PyBankResults.txt")

    # write out results to text file
with open(poll_output, "w") as txtfile:
    txtfile.write("Total Month :" + str(count))
    txtfile.write(("\nTotal : $" + str(total)))
    txtfile.write(("\nAverage Change: $" + str(round(change / (count - 1), 2))))
    txtfile.write(("\nGreatest Increase in Profits:" + str(date[min_index]) + " ( $ " + str(max(changes)) + ")"))
    txtfile.write(("\nGreatest Decrease in Profits:" + str(date[max_index]) + " ( $ " + str(min(changes)) + ")"))
