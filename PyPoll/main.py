import os
import csv

#accessing the election_data.csv file in the Resources folder
election_csvpath = os.path.join("Resources","election_data.csv")

#COMMENT
poll_txtpath = os.path.join("analysis","poll_result.txt")

def election_result(candidate_data):

    #printing the output in a .txt file
    with open(poll_txtpath, "w") as f:
        #print("Election Results")
        print("Election Results", file=f)
        print("", file=f)
        print("------------------------------------------------------", file=f)
        print("", file=f)

        #the total number of votes cast
        total_votes = len(candidate_data)
        #print("Total Votes: " + str(total_votes))
        print("Total Votes: " + str(total_votes), file=f)
        print("", file=f)
        print("------------------------------------------------------", file=f)
        print("", file=f)

        #the list of candidates who received votes, with their vote %, and total number of votes received
        candidates = []
        get_unique = [candidates.append(candidate) for candidate in candidate_data if candidate not in candidates]
        #print(candidates)

        #COMMENT
        counts = [0]*len(candidates)

        #
        for candidate in range(len(candidate_data)):
            if candidate_data[candidate] == candidates[0]:
                counts[0] += 1
                #print(candidates[0])
            elif candidate_data[candidate] == candidates[1]:
                counts[1] += 1
                #print(candidates[1])
            else:
                counts[2] += 1
                #print(candidates[2])

        percentages = [count/total_votes for count in counts]

        #PRINT COMMENT
        for i in range(len(candidates)):
            #print(str(candidates[i]) + ": " + "{:.3%}".format(percentages[i]) + " (" + str(counts[i]) +")")
            print(str(candidates[i]) + ": " + "{:.3%}".format(percentages[i]) + " (" + str(counts[i]) +")", file=f)
        print("", file=f)
        print("------------------------------------------------------", file=f)
        print("", file=f)

        #COMMENT
        results = dict(zip(candidates,percentages))
        #print(results)

        # WINNER COMMENT
        winner = max(percentages)
        index = 0
        for i in range(len(percentages)):
            if percentages[i] == winner:
                index = i
        
        #print("Winner: " + str(candidates[index])) 
        print("Winner: " + str(candidates[index]),file=f)  
        print("", file=f)
        print("------------------------------------------------------", file=f)
        print("", file=f)

        f.close()
        return


#reading the csv file
with open(election_csvpath) as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    election_csvreader = csv.reader(csvfile, delimiter=',')
    #print(election_csvreader)

    #read the header row first
    election_csvheader = next(election_csvreader)
    #print(f"Election Data Header: {election_csvheader}")

    #COMMENT
    candidate_data = []
    for row in election_csvreader:
        candidate_data.append(row[2])
    #print(candidate_data)

election_result(candidate_data)
