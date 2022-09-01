
raw = open("./input/cab_rides.csv", "r")

clean = open("./input/clean_cab.csv", "w")
uber = open("./input/uber.csv", "w")
lyft = open("./input/lyft.csv", "w")

gotHeaders = False
id_index = 0

# text columns: cab_type, placesination, source, product_id, name
# uber = 0; lyft = 1
headers = {}
places = {}
product = {}
name = {}

for line in raw:
    curLine = line.rstrip().split(",")
    if gotHeaders == False:
        for i in range(0, len(curLine)-1):
            headers[i] = curLine[i]
            if(curLine[i] == "id"):
                id_index = i
                continue
            clean.write(curLine[i])
            clean.write(",")
        clean.write(curLine[-1])
        headers[len(headers)] = curLine[-1]
        clean.write("\n")
        gotHeaders = True
        continue
    else:
        for i in range(0, len(curLine)-1):
            if(i != id_index):
                if(headers[i] == "cab_type"):
                    if(curLine[i] == "Uber"):
                        clean.write("0")
                    else:
                        clean.write("1")
                elif(headers[i] == "destination"):
                    if(curLine[i] not in places):
                        places[curLine[i]] = len(places)
                    clean.write(str(places[curLine[i]]))
                elif(headers[i] == "source"):
                    if(curLine[i] not in places):
                        places[curLine[i]] = len(places)
                    clean.write(str(places[curLine[i]]))
                elif(headers[i] == "product_id"):
                    if(curLine[i] not in product):
                        product[curLine[i]] = len(product)
                    clean.write(str(product[curLine[i]]))
                else:
                    clean.write(curLine[i])
                clean.write(",")
        if(curLine[-1]) not in name:
            name[curLine[-1]] = len(name)
        clean.write(str(name[curLine[-1]]))
        clean.write("\n")



clean.close()
raw.close()

all = open("./input/clean_cab.csv", "r")

for line in all:
    l = line.rstrip().split(",")
    if(l[1] == "0"):
        uber.write(line)
    else:
        lyft.write(line)

uber.close()
lyft.close()


# placesination: {'North Station': 0, 
#               'Northeastern University': 1, 
#               'West End': 2, 
#               'Haymarket Square': 3, 
#               'South Station': 4, 
#               'Fenway': 5, 
#               'Theatre District': 6, 
#               'Beacon Hill': 7, 
#               'Back Bay': 8, 
#               'North End': 9, 
#               'Financial District': 10, 
#               'Boston University': 11}
# source: {'Haymarket Square': 0, 
#          'Back Bay': 1, 
#           'North End': 2, 
#           'North Station': 3, 
#           'Beacon Hill': 4, 
#           'Boston University': 5, 
#           'Fenway': 6, 
#           'South Station': 7, 
#           'Theatre District': 8, 
#           'West End': 9, 
#           'Financial District': 10, 
#           'Northeastern University': 11}
# product: {'lyft_line': 0, 
#           'lyft_premier': 1, 
#           'lyft': 2, 
#           'lyft_luxsuv': 3, 
#           'lyft_plus': 4, 
#           'lyft_lux': 5, 
#           '6f72dfc5-27f1-42e8-84db-ccc7a75f6969': 6,       these are uber
#           '6c84fd89-3f11-4782-9b50-97c468b19529': 7, 
#           '55c66225-fbe7-4fd5-9072-eab1ece5e23e': 8, 
#           '9a0e7b09-b92b-4c41-9779-2ad22b4d779d': 9, 
#           '6d318bcc-22a3-4af6-bddd-b409bfce1546': 10, 
#           '997acbb5-e102-41e1-b155-9df7de0a73f2': 11, 
#           '8cf7e821-f0d3-49c6-8eba-e679c0ebcf6a': 12}
# name: {'Shared': 0, 
#       'Lux': 1, 
#       'Lyft': 2, 
#       'Lux Black XL': 3, 
#       'Lyft XL': 4, 
#       'Lux Black': 5, 
#       'UberXL': 6, 
#       'Black': 7, 
#       'UberX': 8, 
#       'WAV': 9, 
#       'Black SUV': 10, 
#       'UberPool': 11, 
#       'Taxi': 12}