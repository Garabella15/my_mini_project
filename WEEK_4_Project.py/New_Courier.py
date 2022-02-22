import csv
import CSV_write
def create_new_Courier():
    from read_file_to_list import read_courier_csv_file
    read_courier_csv_file()
    Courier =[]
    input_Courier_name = str(input('enter name of courier:'))
    input_telephone_number = str(input('enter telephone number:'))

    
    Courier_list_dictionary ={'Name':input_Courier_name, 
                             'telephone':input_telephone_number}
                                
    Courier.append(Courier_list_dictionary)   

    CSV_write.Append_new_courier_to_csv_file('Courier.csv', Courier)
    
    print(Courier)