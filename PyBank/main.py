# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

CSV_PATH = os.path.join('.', 'Resources', 'budget_data.csv')
PL_INDEX = 1

with open(CSV_PATH) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    
    #create variables
    counter = 0
    PandL_Total = 0
    previousPL = None
    agg_cur_change = 0
    prev_change = 0 #change to None if necessary
    Greatest_Increase = 0
    Greatest_Decrease = 0
    
    # Read each row of data after the header
    for row in csvreader:
        # print(type(row), row)
        date = str(row[0])
        current_PL = int(row[PL_INDEX])
        counter = 1 + counter 
        PandL_Total = current_PL + PandL_Total
        
        if previousPL is not None:
            
            current_change = current_PL - previousPL
            agg_cur_change = current_change + agg_cur_change
        
            if current_change > prev_change:
                Greatest_Increase = int(current_change)
            
            if current_change < prev_change:
                Greatest_Decrease = int(current_change)
                
            #prepare for next row
            prev_change = current_change
            
        #prepare for next row
        previousPL = current_PL

#create average variable
average = agg_cur_change / (counter - 1)

#now print to terminal and print to new text file
output_path = os.path.join('.', 'analysis', "output.txt")
with open (output_path, "w") as file:
    Financial_Analysis = (
        "Financial Analysis\n"
        "\n"
        "--------------------------------\n"
        "\n"
        f"Total Months: {counter}\n"
        "\n"
        f"Total: ${PandL_Total}\n"
        "\n"
    )

    print(Financial_Analysis)

    file.write(Financial_Analysis)

    average = agg_cur_change / (counter - 1)
    Average_Change = (
        f"Average Change: ${average: .2f}\n"
        "\n"
    )
    print(Average_Change)
    file.write(Average_Change)
    
    greatest_IandD = (
        f"Greatest Increase in Profits: {date} (${Greatest_Increase})\n"
        "\n"
        f"Greatest Decrease in Profits: {date} (${Greatest_Increase})\n"
    )
    print(greatest_IandD)
    file.write(greatest_IandD)
