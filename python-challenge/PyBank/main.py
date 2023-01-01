import os
import csv

total = 0
count = 0
last = None
last2 = None
change = []
date = []
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    for row in csvreader:
        count += 1
        total += int(row[1])
        if last is not None:
            change.append(int(row[1])-last)
            date.append(row[0])
        last = int(row[1])
    x = max(change)
    z = min(change)

avg = sum(change)/len(change)  

combined = zip(date, change)
for a in combined:
    if a[1] == x:
        max_date = a[0]
    elif a[1] == z:
        min_date = a[0]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {count}")
print(f"Total: ${total}")
print(f"Average Change: ${round(avg, 2)}")
print(f"Greatest Increase in Profits: {max_date} (${x})")      
print(f"Greatest Decrease in Profits: {min_date} (${z})")

output_file = os.path.join("PyBank_output.txt")
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Total Months: {count}"])
    writer.writerow([f"Total: ${total}"])
    writer.writerow([f"Average Change: ${round(avg, 2)}"])
    writer.writerow([f"Greatest Increase in Profits: {max_date} (${x})"])      
    writer.writerow([f"Greatest Decrease in Profits: {min_date} (${z})"])