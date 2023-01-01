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
    for row in csvreader:
        count += 1
        if row[2] not in candidate:
            candidate.append(row[2])
        votes.append(row[2])
        
for name in votes:
    dictionary[name] = dictionary.get(name,0) + 1
   
total_votes = list(dictionary.values())
for percent in total_votes:
    percentage.append(round((percent/count)*100,3))

percent_numbers = [f'{n}%' for n in percentage]
candidate_colon = [f'{c}:' for c in candidate]

summary = zip(candidate_colon,percent_numbers,total_votes)

max_val = max(total_votes)
index = total_votes.index(max_val)
length = len(total_votes)
winner = candidate[index]


print(f"Total Votes: {count}")

for entry in summary:
    print(entry)
print(f"Winner: {winner}")

output_file = os.path.join("analysis", "PyPoll_output.txt")
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Election Results"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Total Votes: {count}"])
    writer.writerow(["----------------------------"])
    writer.writerows(summary)
#    for entry in summary:
#        writer.writerow(entry)
    writer.writerow(["----------------------------"])
    writer.writerow([f"Winner: {winner}"])