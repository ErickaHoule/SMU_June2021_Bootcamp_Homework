# This will allow us to create file paths across operating systems
import os
import numpy as np
import pandas as pd

# Module for reading CSV files
import csv

csvpath = "/Users/erickahoule/Desktop/SMU/Homework - GitHub/SMU_June2021_Bootcamp_Homework/03-Python/PyPoll/election_data.csv"

#Variables
vote_total = 0
votes = {}
candidate = ""

with open(csvpath) as csvfile:

#     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    # print(f'CSV Header: {csv_header}')

    for row in (csvreader):
        vote_total = vote_total + 1
        candidate = row[2]

        if candidate in votes:
            votes[candidate] = votes[candidate] + 1
        else:
            votes[candidate] = 1

print(f'Total Votes: {vote_total}')

# Calculating the % of votes for each candidate
for candidate in votes:
    percentage = round((votes[candidate]/vote_total)*100, 3)

    print(f' {candidate}: " {str(percentage)}% ({str(votes[candidate])})')
    
# Finding the Winner
Winner_name = ""
init_votes = 0
for winner in votes.keys():
    votes_won = votes[winner]
    if votes_won > init_votes:
        init_votes = votes_won 
        Winner_name = winner

print(f'Winner: {Winner_name}')

# write to text file
file = open("SMU_June2021_Bootcamp_Homework/03-Python/PyPoll/PyPoll_Outputs.txt", "w") 
file.write(f'Election Results \n')
file.write(f'------------------------------------------------------\n')
file.write(f'Total: ${vote_total}\n')
file.write(f'------------------------------------------------------\n')
file.write(f'{candidate}: " {str(percentage)}% ({str(votes[candidate])})\n')
file.write(f'------------------------------------------------------\n')
file.write(f'Winner: {Winner_name}\n')
file.write(f'------------------------------------------------------')
file.close() 