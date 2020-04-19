# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculte the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote. 

## Resources
- Data Sources: election_results.csv
- Software: Python 3.8.2, Visual Studio Code, 1.44.2

## Summary
The analysis of the election show that:
- There were "x" votes cast in the election.
- The candidates were:
    - Candidate 1
    - Candidate 2
    - Candidate 3
- The candidate results were:
    - Candidate 1 received "x%" of the vote and "y number of votes.
    - Candidate 2 received "x%" of the vote and "y number of votes.
    - Candidate 3 received "x%" of the vote and "y number of votes.
- The winner of the election was:
    - Candidate (1, 2, or 3), who received "x%" of the vote and "y number of votes.
    
## Challenge Overview
**The goals of this challenge are for you to:**

*1. Extend your use of "for" loops and conditionals with membership and logical operators.
2. Scope and refactor code to provide additional information.
3. Write data to an output file and print the file.*

## Challenge Summary
1. We have updated formatting of the election_analysis.txt with newly added "County Votes:".
2. The county votes have been established based on similar "for" loop structure as the candidate votes.
3. The comparison of each county's votes is based on a similar if-statement inside a "for" loop, mimicking the strategy to determine the highest winning voter.
4. Added space above and below the county vote summary emphasises the newly added analysis.
5. The newly-added breakline and "Largest County Turnout: "z"" has been displayed based on the votes results.
