import csv
def read_csv(file_name):
    courier = []
    with open(file_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            courier.append(row)
    print (courier)

    for index, row in enumerate(courier):
        print(index, row)
    input_courier_index=int(input('enter index of courier:'))
    courier.pop(input_courier_index)

    with open(file_name, mode ='w') as file:
        
        fieldnames = ['Name', 'telephone']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(courier)
        print(courier)  
    

