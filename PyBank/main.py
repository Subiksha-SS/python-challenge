# Modules
import os
import csv

csvpath = os.path.join ("Resources", "budget_data.csv")

# open CSV file
with open(csvpath) as csvfile:

    # CSV reader, specifying delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csvheader = next(csvreader)

    # variable to store total number of months
    totalmonths = 0
    # variable to store net total amount of "Profit/Losses"
    total = 0

    # list to store the differences between the profit/losses over the entire period 
    differences=[]
    
    # list to store the dates
    current_date=[]
    # list to store the values of the profit/losses
    current_prof_loss= []
            
    for row in csvreader:
        
        # counting total number of months in the dataset
        totalmonths= totalmonths + 1

        # Calculate the net total amount of "Profits/Losses"
        total = total + int(row[1])    

        # adding date to a list
        current_date.append(row[0])

        # adding profit/loss value to list
        current_prof_loss.append(int(row[1]))
        
    
    #length of the list containing Profits/Losses over entire period
    length_of_list = len(current_prof_loss)    

    # loop through Profits/Losses to calculate the difference between each month and store them in the differences list
    for x in range (1,length_of_list):
        differences.append(current_prof_loss[x] - current_prof_loss[x-1])
    
    # calculating the average of the changes over the entire period
    totaldiff = sum(differences) / len(differences)

    # setting greatest increases and decreases
    greatest_increase = max(differences)
    greatest_decrease = min(differences)

    # finding the date of greatest increase and decrease in profits        
    date_increase= differences.index(greatest_increase) + 1
    date_decrease= differences.index(greatest_decrease) + 1

# Storing results in list
lines=["Financial Analysis", "-----------------------------------", f"Total Months: {totalmonths}", f"Total: ${total}", 
       f"Average Change: ${(round(totaldiff,2))}", f"Greatest Increase in Profits: {current_date[date_increase]} (${greatest_increase})", 
       f"Greatest Decrease in Profits: {current_date[date_decrease]} (${greatest_decrease})"]

# writing a txt file
with open ('analysis\pybank_results.txt', 'w') as f:
    # writing the results from the list
    for l in lines:
        f.write(l)
        f.write('\n')

# printing results to Terminal
print ("Financial Analysis\n")
print ("-----------------------------------\n")
print (f"Total Months: {totalmonths}\n")
print (f"Total: ${total}\n")
print (f"Average Change: ${(round(totaldiff,2))}\n")
print (f"Greatest Increase in Profits: {current_date[date_increase]} (${greatest_increase})\n")
print (f"Greatest Decrease in Profits: {current_date[date_decrease]} (${greatest_decrease})\n")
