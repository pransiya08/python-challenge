import os
import csv

#accessing the budget_data.csv file in the Resources folder
budget_csvpath = os.path.join("Resources","budget_data.csv")

#COMMENT
analysis_txtpath = os.path.join("analysis","analysis_result.txt")

#defining the analyse_budget() function
def analyse_budget(month_data, budget_data):

    #printing the output in a .txt file
    with open(analysis_txtpath, "w") as f:
        print("Financial Analysis", file=f)
        print("------------------------------------------------------", file=f)
    
        #the total number of months included in the dataset can be identified by getting the length of the budget data (1 month: 1 p/l)
        total_month = len(month_data)
        print("Total Months: " + str(total_month), file=f)

        #the net total amount of "Profit/Losses" over the entire period
        nettotal_PL = 0
        for budget in budget_data:
            nettotal_PL += int(budget)
        print("Total: $"+"{:,.2f}".format(nettotal_PL), file=f)  

        #the changes in "Profit/Losses" over the entire period, and then the average of those changes
        change_PL = []

        #COMMENT
        for x in range(1,total_month):
            diff = int(budget_data[x]) - int(budget_data[x-1])
            change_PL.append(diff)
        #print(change_PL)

        #COMMENT
        changetotal_PL = 0
        for change in change_PL:
            changetotal_PL += int(change)
        changeave_PL = changetotal_PL/(total_month-1)
        print("Average Change: $"+"{:,.2f}".format(changeave_PL), file=f) 

        #the greatest increase in profits (date and amount) over the entire period
        max_PL = max(change_PL)
        #COMMENT       
        for budget in range(0,total_month-1):
            if max_PL == change_PL[int(budget)]:
                max_month = str(month_data[int(budget+1)])
        print("Greatest Increase in Profits: " + (max_month) + " ($"+"{:,.2f}".format(max_PL)+")", file=f)


        #the greatest decrease in profits (date and amount) over the entire period
        min_PL = min(change_PL)
        #COMMENT    
        for budget in range(0,total_month-1):
            if min_PL == change_PL[int(budget)]:
                min_month = str(month_data[int(budget+1)])
        print("Greatest Decrease in Profits: " + (min_month) + " ($"+"{:,.2f}".format(min_PL)+")", file=f)

        #COMMENT
        f.close()

        return 


#reading the csv file
with open(budget_csvpath) as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    budget_csvreader = csv.reader(csvfile, delimiter=',')
    #print(budget_csvreader)

    #read the header row first
    budget_csvheader = next(budget_csvreader)
    #print(f"Budget Data Header: {budget_csvheader}")

    #COMMENT
    budget_data = []
    month_data = []
    for row in budget_csvreader:
        month_data.append(row[0])
        budget_data.append(row[1])

analyse_budget(month_data, budget_data)
