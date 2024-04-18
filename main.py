import os
import csv

csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')
csvreader = csvpath

#define how many votes we are starting with 
total_votes = 0
candidate_votes = {}
vote_count = {}

#open and read csv
with open(csvpath) as csv_file:
    csv_reader = csv.reader (csv_file, delimiter=",")
#skipping header row 
    next(csv_reader)


#go through each row. if name is the same from above add one, if it is different start at 0. this will find who has votes and how many
    for row in csv_reader:
        total_votes += 1
        name = row[2]

        if name in candidate_votes.keys():
            candidate_votes[name] += 1  
        else:
            candidate_votes[name]=1
    output_analysis= "Election Results\n---------------\n"
    output_analysis+=f'Total Votes: {total_votes}\n--------------\n'

max_votes = 0
winner = "name"

#find percent of votes each candidate got
for candidate, votes in candidate_votes.items():
    percentage = (votes/total_votes)*100

    output_analysis+=f'{candidate}: {percentage:.3f}% ({votes})\n'
    if votes > max_votes:
        max_votes = votes
        winner = candidate

output_analysis+= "--------------\n"
output_analysis+=f'winner:{winner}\n'
output_analysis+= "--------------\n"
print(output_analysis)



output_path = os.path.join("PyPoll", "Analysis", "textfile.txt")
# Initialize csv.writer
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
 # Write the second row
    csvwriter.writerow(['Chelsea', 'Cullen', 'homework3'])
    # Write the first row (column headers)
    csvwriter.writerow({output_analysis})
                       
   
