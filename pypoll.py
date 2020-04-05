import pandas as pd
import os
import csv


voter_id = []
county = []
candidate = []
unique_candidate = []
vote_count = []
vote_percent=[]
count=0

df= os.path.join("","election_data.csv")

with open(df) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csvheader = next(csvreader)


    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        count += 1

    for i in set(candidate):
        unique_candidate.append(i)
        y=candidate.count(i)
        vote_count.append(y)
        vote_percent.append((y/count)*100)

winning_vote_count = max(vote_count)
winner = unique_candidate[vote_count.index(winning_vote_count)]

print("Election Results")
print("-------------------------")
print("Total Votes: "+str(count))
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

poll_output = os.path.join("PyPollResults.txt")

# write out results to text file
with open(poll_output, "w") as txtfile:
    txtfile.write("\nElection Results")
    txtfile.write("\n-------------------------")
    txtfile.write("\nTotal Votes: " + str(count))
    for i in range(len(unique_candidate)):
        txtfile.write("\n"+unique_candidate[i] + ": " + str(vote_percent[i]) + "% (" + str(vote_count[i]) + ")")
    txtfile.write("\n-------------------------")
    txtfile.write("\nThe winner is: " + winner)
    txtfile.write("\n-------------------------")
