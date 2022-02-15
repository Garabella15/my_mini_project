import csv
def read_csv(filename):
    
    list_item =[]
    with open(filename) as file:
        reader=csv.DictReader(file)
        for row in reader:
            list_item.append(row)
    return list_item
    