import os
import csv

#accessing the budget_data.csv file in the Resources folder
budget_csvpath = os.path.join("Resources","budget_data.csv")

#creating the txt file and path for the result of the analysis
analysis_txtpath = os.path.join("analysis","budgetanalysis_result.txt")

#creating the analyse_budget() function
def analyse_budget(month_data, budget_data):

    #printing the output in a .txt file
    with open(analysis_txtpath, "w") as f:
        print("",file=f)
        print("Financial Analysis", file=f)
        print("",file=f)
        print("------------------------------------------------------", file=f)
        print("",file=f)
    
        #the total number of months included in the dataset can be identified by getting the length of the budget data (1 month: 1 p/l)
        total_month = len(month_data)
        #print(total_month) #check the total month result
        print("Total Months: " + str(total_month), file=f)
        print("",file=f)

        #calculating the net total amount of "Profit/Losses" over the entire period
        nettotal_PL = 0
        #creating a for loop to sum up the monthly budget over the entire period and printing the final/total budget
        for budget in budget_data:
            nettotal_PL += int(budget)
        #print(netotal_PL) #check the final budget total result
        print("Total: $"+"{:,.2f}".format(nettotal_PL), file=f) 
        print("",file=f) 

        #caluclating the changes in "Profit/Losses" over the entire period, and then the average of those changes
        change_PL = []
        #creating a for loop to store the changes between the current and previous month in an array
        for x in range(1,total_month):
            diff = int(budget_data[x]) - int(budget_data[x-1])
            change_PL.append(diff)
        #print(change_PL) #check the change array results

        #calculating the average change for the entire period 
        changetotal_PL = 0
        #creating a for loop to sum up the total changes over the entire period then getting the average
        for change in change_PL:
            changetotal_PL += int(change)
        changeave_PL = changetotal_PL/(total_month-1)
        #print(changeave_PL) #check the average change result
        print("Average Change: $"+"{:,.2f}".format(changeave_PL), file=f)
        print("",file=f) 

        #identify the greatest increase in profits (date and amount) over the entire period
        max_PL = max(change_PL)
        #creating a for loop to check all rows and match with the identified max change and print the corresponding month     
        for budget in range(total_month-1):
            if max_PL == change_PL[int(budget)]:
                max_month = str(month_data[int(budget+1)])
        #print(max_month , max_PL) check the max month and change results         
        print("Greatest Increase in Profits: " + (max_month) + " ($"+"{:,.2f}".format(max_PL)+")", file=f)
        print("",file=f)


        #identify the greatest decrease in profits (date and amount) over the entire period
        min_PL = min(change_PL)
        #creating a for loop to check all rows and match with the identified min change and print the corresponding month  
        for budget in range(0,total_month-1):
            if min_PL == change_PL[int(budget)]:
                min_month = str(month_data[int(budget+1)])
        #print(min_month , min_PL) check the min month and change results
        print("Greatest Decrease in Profits: " + (min_month) + " ($"+"{:,.2f}".format(min_PL)+")", file=f)

        return 


#reading the csv file
with open(budget_csvpath) as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    budget_csvreader = csv.reader(csvfile, delimiter=',')
    #print(budget_csvreader)

    #read the header row first
    budget_csvheader = next(budget_csvreader)
    #print(f"Budget Data Header: {budget_csvheader}")

    #getting the necessary data from the csv file
    budget_data = []
    month_data = []
    for row in budget_csvreader:
        month_data.append(row[0])
        budget_data.append(row[1])

#running the function analyse_budget
analyse_budget(month_data, budget_data)