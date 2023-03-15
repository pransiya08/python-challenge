import os
import csv

#accessing the election_data.csv file in the Resources folder
election_csvpath = os.path.join("Resources","election_data.csv")

#creating the txt file and path for the result of the poll
poll_txtpath = os.path.join("analysis","pollanalysis_result.txt")

#creating the election_result() function
def election_result(candidate_data):

    #printing the output in a .txt file
    with open(poll_txtpath, "w") as f:
        print("Election Results", file=f)
        print("", file=f)
        print("------------------------------------------------------", file=f)
        print("", file=f)

        #calculate the total number of votes cast
        total_votes = len(candidate_data)
        #print(total_votes) #check the total vote result
        print("Total Votes: " + str(total_votes), file=f)
        print("", file=f)
        print("------------------------------------------------------", file=f)
        print("", file=f)

        #get the list of unique candidates included in the election/poll
        candidates = []
        get_unique = [candidates.append(candidate) for candidate in candidate_data if candidate not in candidates]
        #print(candidates)

        #setting up the array for the vote counts
        counts = [0]*len(candidates)

        #creating a for loop to add a vote count to a candidate by matching up with them in the candidates array
        for candidate in range(len(candidate_data)):
            if candidate_data[candidate] == candidates[0]:
                counts[0] += 1
            elif candidate_data[candidate] == candidates[1]:
                counts[1] += 1
            else:
                counts[2] += 1

        #calculating the percentage of the total votes received by a candidate
        percentages = [count/total_votes for count in counts]

        #creating a for loop to print out the candidates who received votes, with their vote %, and total number of votes received from the calculated arrays above
        for i in range(len(candidates)):
            print(str(candidates[i]) + ": " + "{:.3%}".format(percentages[i]) + " (" + str(counts[i]) +")", file=f)
        print("", file=f)
        print("------------------------------------------------------", file=f)
        print("", file=f)

        #identifying the winner by getting the max vote% (vote count can be used too)
        winner = max(percentages)
        #creating a for loop to identify the index of the max vote% in the percentages array to identify which candidate it corresponds to
        index = 0
        for i in range(len(percentages)):
            if percentages[i] == winner:
                index = i
        
        #print(candidates[index]) #to check the winner 
        print("Winner: " + str(candidates[index]),file=f)  
        print("", file=f)
        print("------------------------------------------------------", file=f)
        print("", file=f)

        return


#reading the csv file
with open(election_csvpath) as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    election_csvreader = csv.reader(csvfile, delimiter=',')
    #print(election_csvreader)

    #read the header row first
    election_csvheader = next(election_csvreader)
    #print(f"Election Data Header: {election_csvheader}")

    #getting the necessary data from the csv file
    candidate_data = []
    for row in election_csvreader:
        candidate_data.append(row[2])
    #print(candidate_data)

#running the function election_result
election_result(candidate_data)