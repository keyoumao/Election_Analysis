counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
{"county":"Denver", "registered_voters": 463353},
{"county":"Jefferson", "registered_voters": 432438}]

for county, voters in counties_dict.items():
#     print(str(county) + " county has " + str(voters) + " registered voters. ")
    print(f"{county} county has {voters} registered voters.") 

dic_1 = voting_data[0]
print(dic_1)
trial = dic_1.values()
print(trial)


for data in voting_data:
    
    county, voters = data.values()
    
    print(f"{county} county has {voters} registered voters.") 
  
