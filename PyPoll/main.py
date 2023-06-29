# Modules
import os
import csv

# Specify file to read from
csvpath = os.path.join("Resources", "election_data.csv")

# Open CSV file
with open(csvpath) as csvfile:
    # csv reader specifying delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # read the header row first
    csv_header = next(csvreader)
    
    # variable to store the total number of votes
    totalvotes = 0

    # list that contains the vote for each candidate
    candidates = []

    # read each row in data after header,counting votes and adding candidates to list
    for row in csvreader:
        totalvotes = totalvotes + 1
        candidates.append(row[2])
    
    # 
    with open('analysis\election_results.txt', 'w') as f:
         
        print ("Election Results\n")
        f.write ("Election Results\n")
        print ("--------------------------\n")
        f.write ("--------------------------\n")
        
        print (f"Total Votes: {totalvotes}\n")
        f.write(f"Total Votes: {totalvotes}\n")
        print ("--------------------------\n")
        f.write ("--------------------------\n")
        

        # dictionary to store candidates and their total votes
        final_c = {}

        #adding candidates to dictionary with their total votes
        for x in candidates:
            if x in final_c:
                final_c[x] += 1
            else:
                final_c[x] = 1
        
        # variable to store the winning candidate
        winner = ""
        win_vote = 0
        
        # reading through dictionary of candidates with total votes 
        for candidate in final_c:
            votes = final_c[candidate]
            vote_percentage = round (votes / totalvotes * 100, 3)
            
            # printing the candidates, total percentage of votes and total votes
            print (f"{candidate}: {vote_percentage}% ({votes})\n")
            # printing results to txt file
            f.write(f"{candidate}: {vote_percentage}% ({votes})\n")

            # determine the greatest number of total votes and its candidate
            if votes > win_vote:
                win_vote = votes
                winner = candidate
        
        print ("--------------------------\n")
        f.write ("--------------------------\n")
        print (f"Winner: {winner}\n")
        f.write (f"Winner: {winner}\n")
        print ("--------------------------")
        f.write ("--------------------------\n")


        

