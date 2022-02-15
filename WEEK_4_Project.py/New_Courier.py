def create_new_Courier():
    import csv
    import CSV_write
    input_Courier_name = str(input('enter name of Courier:'))
    input_Courier_telephone = str(input('enter phone number:'))

    from read_file_to_list import read_csv
    Courier_list = read_csv('Courier.csv')
    
    Courier_list_dictionary ={'Name': input_Courier_name, 
                                'telephone': input_Courier_telephone}
                                
    Courier_list.append(Courier_list_dictionary)   

    CSV_write.write_list_of_Courier_dict_to_csv('Courier.csv', Courier_list)
    
    print(Courier_list) 