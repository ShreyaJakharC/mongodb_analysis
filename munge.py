import csv
data_1 = open("data/listings.csv", "r")
reader = csv.reader(data_1)
final_data = open("data/listings_clean.csv", "w")
writer = csv.writer(final_data)

information = []
new_information = []
for info in reader:
    information.append(info)

x = 0

while x < len(information):
    if information[x][13] == "": 
        x += 1
        continue
    else:
        new_information.append(information[x])
        x += 1
     



    
    


for info_1 in new_information:
    writer.writerow(info_1)



data_1.close()
final_data.close()