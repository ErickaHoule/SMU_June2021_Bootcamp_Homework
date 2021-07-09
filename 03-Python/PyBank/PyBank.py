# This will allow us to create file paths across operating systems
import os
import numpy as np

# Module for reading CSV files
import csv

csvpath = "SMU_June2021_Bootcamp_Homework/03-Python/PyBank/budget_data.csv"

with open(csvpath) as csvfile:

#     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    # print(f'CSV Header: {csv_header}')

    # stor all rows as a list of lists
    all_rows = []
    for row in csvreader:
        # change Profit/Losses from string to integer
        temp_row = row
        temp_row[1] = int(temp_row[1])

        all_rows.append(row)
   
# print # of months
total_months =(len(all_rows))
print(f'Total Months: {total_months}')

# Sum of Profit/Losses
total_PL = sum([row[1] for row in all_rows])
print(f'Total: ${total_PL}')

changes = []
for i in range(len(all_rows) - 1):
    curr_profit = all_rows[i][1]
    next_profit = all_rows[i+1][1]

    change = next_profit - curr_profit
    changes.append(change)

average_change = sum(changes)/len(changes)
round_ac = round(average_change,2)
print(f'Average Change: ${round_ac}')

# Greatest Increase in profits: Max value & max value index
max_value = max(changes)
index_max = changes.index(max_value) + 1
index_month = (all_rows[index_max][0])
print(f'Greatest Increase in Profits: {index_month} (${max_value})')

# Greatest decrease in profits: Min value & min value index
min_value = min(changes)
index_min = changes.index(min_value) + 1
min_month = (all_rows[index_min][0])
print(f'Greatest Decrease in Profits: {min_month} (${min_value})')


file = open("SMU_June2021_Bootcamp_Homework/03-Python/PyBank/PyBank_Outputs.txt", "w") 
file.write(f'Financial Analysis\n')
file.write(f'------------------------------------------------------\n')
file.write(f'Total: ${total_PL}\n')
file.write(f'Total: ${total_PL}\n')
file.write(f'Average Change: ${round_ac}\n')
file.write(f'Greatest Increase in Profits: {index_month} (${max_value})\n')
file.write(f'Greatest Decrease in Profits: {min_month} (${min_value})')
file.close() 