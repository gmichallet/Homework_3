#import 
import csv
filename="budget_data.csv"

#output
text_path = "output.txt"

#Define variables
P = []
months = []
revenue_change = []

# open and read csv
with open('budget_data.csv') as csvfile:  
    csvreader = csv.DictReader(csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    #Skip header row
    print(f"Header: {csv_header}")

    #To read each row of data after header
    for rows in csvreader:
        P.append(int(rows[1]))
        months.append(rows[0])

    #The total number of months included in the dataset
    total_months = len(months)

    #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    for x in range(1, len(P)):
        revenue_change.append((int(P[x]) - int(P[x-1])))
    
    revenue_average = sum(revenue_change) / len(revenue_change)

    #The greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(revenue_change)

    #The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(revenue_change)


    #Print Results
    print("Financial Analysis")
    print("..................................................")
    print("Total Months: " + str(total_months))
    print("Total: " + "$" + str(sum(P)))
    print("Average change: " + "$" + str(revenue_average))
    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))

#write to the output text file
with open(text_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("....................\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Revenue: " + "$" + str(sum(P)) + "\n")
    file.write("Average Revenue Change $%d\n" % revenue_average)
    file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")
    file.write("Greatest Decrease in Profits: "+ str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")