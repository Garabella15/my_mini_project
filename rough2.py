def delete_Courier_list ():
    input_Courier_index = int(input('enter Courier index:'))
    Courier_list = open('Courier.txt', 'r')
    lines = Courier_list.readlines()
    Courier_list.close()
    
    del lines[input_Courier_index]
    
    with open('Courier.txt', 'w+') as Courier_list:
        for line in lines:
	        Courier_list.writelines(line)






