
#The data we need to retrieve.
#1. The total number of votes to cast
#2. A complete list of candidates who received votes
#3. the Percentage of votes each candidate who
#4. the total number of votes each candidate won
#5. the winner of the election based on popular vote.

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    
    # Write three counties to the file.
     txt_file.write("Arapahoe, ")
     txt_file.write("Denver, ")
     txt_file.write("Jefferson")

# Close the file
outfile.close()