import os
import csv

# set path to election_data csv
election_data_csv = os.path.join("Resources", "election_data.csv")

# Create variables
total_number_of_votes = 0
candidates_receiving_votes = {}
most_votes = 0
election_winner = ""

# Import the election_data
with open(election_data_csv, "r",) as csvfile:
    election_data_reader = csv.reader(csvfile, delimiter=",")

    # Skip header
    csv_header = next(election_data_reader)

    # Loop through the rows
    for row in election_data_reader:
        # Count the total votes
        total_number_of_votes += 1
        # Get candidate name from the row
        candidate_name = row[2]
        # Update candidate dictionary with corrosponding candidate_name and vote count
        candidates_receiving_votes[candidate_name] = candidates_receiving_votes.get(candidate_name, 0) + 1

# Find election winner
for candidate, votes in candidates_receiving_votes.items():
    if votes > most_votes:
        most_votes = votes
        election_winner = candidate

# Print Terminal restults
print("Election Results")
print("-" * 35)

# Check total number of votes
print(f'Total Votes: {total_number_of_votes}')
print("-" * 35)

# Calculate and print the percentage of votes for each candidate that received votes
for candidate, votes in candidates_receiving_votes.items():
    percentage = (votes / total_number_of_votes) * 100
    print(f'{candidate}: {round(percentage, 3)}% ({votes})')
print("-" * 35)

# Print the winner
print("Winner: " + election_winner)
print("-" * 35)

# Set the file output
election_analysis_output_file = os.path.join("Analysis", "Election Analysis.txt")

# Write text file
with open(election_analysis_output_file, "w", encoding="utf-8") as f:
    f.write("Election Results\n")
    f.write("-" * 35 + "\n")
    f.write(f'Total Votes: {total_number_of_votes}\n')
    f.write("-" * 35 + "\n")
    for candidate, votes in candidates_receiving_votes.items():
            percentage = (votes / total_number_of_votes) * 100
            f.write(f'{candidate}: {round(percentage, 3)}% ({votes})\n')
    f.write("-" * 35 + "\n")
    f.write("Winner: " + election_winner + "\n")
    f.write("-" * 35 + "\n")
