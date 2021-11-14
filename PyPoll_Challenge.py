# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("..", "Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.

file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# County Options
county_options = []
#County_dictionary
county_votes = {}
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate...
        if county_name not in county_options:
            # Add it to the list of candidates.
            county_options.append(county_name)

            # Begin tracking that candidate's vote count.
            county_votes[county_name] = 0

        # Add a vote to that candidate's count
        county_votes[county_name] += 1


# Print the candidate vote dictionary.
print(county_votes)

# Print the candidate list.
print(county_options)


# Track the winning candidate, vote count and percentage
largest_county = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for county_name in county_votes:
    # Retrieve vote count of a candidate.
    votes = county_votes[county_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         largest_county = county_name
         
         print(f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")

         largest_county_summary = (
    f"-------------------------\n"
    f"Largest County Turnout: {largest_county}\n"
    f"-------------------------\n")
print(largest_county_summary)


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row. While reading the election results 
        # from each row inside the for loop, write a script that gets the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes.append[county_name]

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
for key,value in county_votes.items():
    print (key)
        # 6b: Retrieve the county vote count.
for key,value in county_votes.items():
    print(value)
        # 6c: Calculate the percentage of votes for the county.
for county_name in county_votes:
  
    votes = county_votes[county_name]
   
    vote_percentage = float(votes) / float(total_votes) * 100
    
    print(f"{county_name}: received {vote_percentage}% of the vote.")

         # 6d: Print the county results to the terminal.

    print(county_votes)


         # 6e: Save the county votes to a text file.
txt_file.write(county_name)

         # 6f: Write an if statement to determine the winning county and get its vote count.
votes = county_votes[county_name]
vote_percentage = float(votes) / float(total_votes) * 100
if (votes > winning_count) and (vote_percentage > winning_percentage):
    winning_count = votes
    winning_percentage = vote_percentage
    winning_county = county_name

    winning_county_summary = (
    f"-------------------------\n"
    f"Winner: {winning_county}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_county_summary)
    # 7: Print the county with the largest turnout to the terminal.

    winning_county_summary = (
    f"-------------------------\n"
    f"Winner: {winning_county}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
