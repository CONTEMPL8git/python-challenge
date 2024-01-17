# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
CSV_PATH = os.path.join('.', 'Resources', 'election_data.csv')
#PyPoll/Resources

with open(CSV_PATH) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    counter = 0
    candidates = []
    candidate_votes = {}
        # Read each row of data after the header
    for row in csvreader:
        #type(row), row)
        counter = 1 + counter 
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1
output_path = os.path.join('.', 'analysis', "output.txt")
with open (output_path, "w") as file:
    election_results = (
        "Election Results\n"
        "\n"
        "--------------------------------\n"
        "\n"
        f"Total Votes: {counter}\n"
        "\n"
        "--------------------------------\n"
    )

    print(election_results)

    file.write(election_results)
    
    for candidate in candidate_votes:
        votes = candidate_votes.get (candidate)
        percent = votes / counter * 100
        candidate_output = f"{candidate}: {percent:.3f}% ({votes})\n"
        print(candidate_output)
        
        file.write(candidate_output)
    print("--------------------------------\n")
    print("\n")
    