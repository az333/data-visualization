import csv

input_file = csv.DictReader(open("FIREARMS2016.csv"))

data = dict()

for row in input_file:
    del row["URL"]
    state = row["STATE"]
    del row["STATE"]
    data[state] = row

thing = ["HI", "AK", "FL", "SC", "GA", "AL", "NC", "TN", "RI", "CT", "MA",
	 "ME", "NH", "VT", "NY", "NJ", "PA", "DE", "MD", "WV", "KY", "OH", 
	 "MI", "WY", "MT", "ID", "WA", "DC", "TX", "CA", "AZ", "NV", "UT", 
	 "CO", "NM", "OR", "ND", "SD", "NE", "IA", "MS", "IN", "IL", "MN", 
	 "WI", "MO", "AR", "OK", "KS", "LS", "VA"]

print data
