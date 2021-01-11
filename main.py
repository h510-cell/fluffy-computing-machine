import csv
data = []
with open("aagamhem.csv", "r") as f:
csvreader = csv.reader(f)
for row in csvreader:
    data.append(row)
    headers = data[0]
    new_stars_data = data[1:]
#Converting all planet names to lowercase
for data_point in new_stars_data:
    data_point[0] = data_point[0].lower()
#Sorting planet names in alphabetical order
new_stars_data.sort(key=lambda new_stars_data: new_stars_data[0])
df.to_csv("aagamhem_sorted.csv")
with open("aagamhem_sorted.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(new_stars_data)