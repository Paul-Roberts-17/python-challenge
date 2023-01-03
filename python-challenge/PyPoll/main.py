import os
import csv

count = 0
candidate = []
votes = []
dictionary = {}
percentage = []
max_index = 0
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    # count the total amount of votes
    # copy the candidates name into a list without duplicates
    # put all of the votes into a list
    for row in csvreader:
        count += 1
        if row[2] not in candidate:
            candidate.append(row[2])
        votes.append(row[2])

# convert the list of votes into a dictionary, candidate and the count of their votes
for name in votes:
    dictionary[name] = dictionary.get(name,0) + 1

# seperate the total of each candidates votes into a list
# use the total of each candidates votes to calculate the percentage against the vote count   
total_votes = list(dictionary.values())
for percent in total_votes:
    percentage.append(round((percent/count)*100,3))

# formating = add % symbol to percentages, add colon after candidate name
percent_numbers = [f'{n}%' for n in percentage]
candidate_colon = [f'{c}:' for c in candidate]

# zip the lists for candidate, percentage and votes into a list of tuples
summary = zip(candidate_colon,percent_numbers,total_votes)

# find the highest amount of votes in the votes list and use its index to match it to the candidate
max_val = max(total_votes)
index = total_votes.index(max_val)
winner = candidate[index]

# print analysis to terminal
print(f"Total Votes: {count}")
summary_list = []
for entry in summary:
    print(entry)
    summary_list.append(entry)
print(f"Winner: {winner}")

# write analysis to the output text file
output_file = os.path.join("analysis", "PyPoll_output.txt")
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Election Results"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Total Votes: {count}"])
    writer.writerow(["----------------------------"])
    writer.writerows(summary_list)
    writer.writerow(["----------------------------"])
    writer.writerow([f"Winner: {winner}"])