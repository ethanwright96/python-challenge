import os
import csv

#Name file path 
file_path = os.path.join("Resources", "election_data.csv")

#Read csv file
with open (file_path) as poll:
    csv_reader=csv.reader(poll,delimiter=",")
    next(csv_reader)

    #Create empty lists to later append
    id = []
    county = []
    candidates = []

    #Write for loop to append empty lists
    for row in csv_reader:
        id.append((row[0]))
        county.append((row[1]))
        candidates.append((row[2]))
    
#Find the total number of votes using the length of the "Ballot ID" column
total_votes = len(id)

#Create a list of the candidates who received votes 
#Pseudocode: If the current candidate name is not equal to any of those already appended to unique_candidates, then append it to the list

def unique_obs(list):
      unique = []
      for obs in list:
          if obs not in unique:
              unique.append(obs)
      return unique

unique_candidates = unique_obs(candidates)

#Define a user function to output a list of each candidates vote count
#Pseudocode: If the candidate name is equal to option a, count 1 toward option a's count (for a, b, and c)

def counter(list,a,b,c):
    count_a = 0
    count_b = 0
    count_c = 0
    for obs in list:
        if obs == a:
            count_a = count_a + 1
        elif obs == b:
            count_b = count_b + 1
        else: count_c = count_c + 1

    return [count_a,count_b,count_c]

#Use counter function to harvest vote counts for each candidate in list form
vote_counts = counter(candidates,unique_candidates[0],unique_candidates[1],unique_candidates[2])

#Find the winner's name by indexing
max_votes = max(vote_counts)
winner_index = vote_counts.index(max_votes)
winner_name = unique_candidates[winner_index]

#Define percentage function
def percent(part,sum):
     percentage = round(100*part/sum,3)
     return percentage

#Create a list of percentages corresponding with the other vector's indexes
percentages = []
for i in vote_counts:
    percentages.append(percent(i,total_votes))

#Concatenate results and assign to variable name "results"
results = ("Election Results:"
f"\nTotal Votes: {total_votes}"
f"\n{unique_candidates[0]}: {percentages[0]}% ({vote_counts[0]})"
f"\n{unique_candidates[1]}: {percentages[1]}% ({vote_counts[1]})"
f"\n{unique_candidates[2]}: {percentages[2]}%  ({vote_counts[2]})"
f"\nWinner: {winner_name}!")

print(results)

#Write results into .txt file, joining path with analysis folder and file name
with open (os.path.join("analysis","election_results.txt"), 'w') as file:
    file.write(results)
    file.close()
    pass

