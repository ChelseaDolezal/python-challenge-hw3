import os
import csv

#path to collect data from resources folder
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

#define variables
total_months = 0
total_profits = 0
max_value = float('-inf')
max_date = None
min_value = float("inf")
min_date = None
current_profit = 0
total_change_in_profit = 0
is_first_row = True

#open and read csv
with open(csvpath) as csv_file:
    csv_reader = csv.reader (csv_file, delimiter=",")
#skipping header row 
    next(csv_reader)


#for loop to go thru each row to add months, adds profit and losses together
    for row in csv_reader:
        last_month_profit = current_profit
        total_months += 1
        current_profit = float(row[1])
        total_profits += current_profit

#find max value in the set     
        date = row[0]
        #current month-last month
        
        change_in_profit = current_profit - last_month_profit
        if not is_first_row:
            total_change_in_profit += change_in_profit
        else: 
            is_first_row = False
         

        if change_in_profit > max_value:
            max_value = change_in_profit
            max_date = date
#find min value in the set
        date = row[0]
        if change_in_profit < min_value:
            min_value = change_in_profit
            min_date = date


#ask about the first part of Q 3 in hw assignment
    average = total_change_in_profit / (total_months-1)





#creating variable to store outanalysis for future printing.
    output_analysis= "Financial Analysis\n-----------\n"
    output_analysis+=f'Total Months= {total_months}\n'
    output_analysis+=f'Total= ${total_profits}\n'
    output_analysis+=f'Average Change= ${average: .2f}\n'
    output_analysis+=f'Greatest Increase in Profits= {max_date} (${max_value})\n'
    output_analysis+=f'Greatest Decrease in Profits= {min_date} (${min_value})\n'
    print(output_analysis)   

output_path = os.path.join("PyBank", "Analysis", "textfile.txt")
# Initialize csv.writer
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
 # Write the second row
    csvwriter.writerow(['Chelsea', 'Cullen', 'homework3'])
    # Write the first row (column headers)
    csvwriter.writerow({output_analysis})
                       
   
