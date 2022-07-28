import csv
with open('villains.csv','rt') as fin :
    cin = csv.DictReader(fin)
    villains = [row for row in cin]
    
print(villains)