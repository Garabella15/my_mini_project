def delete_Courier_list ():
    Courier_list = display('Courier.txt')
    input_Courier_index = int(input('enter Courier index:'))
    Courier_list.pop(input_Courier_index)
    
    with open('Courier.txt', 'w') as file:
	    file.writelines(Courier_list.pop)

    
def display(filename):
    # filename = input('Enter name of File: ')
    content_list = []
    # try:
    fo = open(filename, "r")
    lines = fo.readlines()
    for line in lines:
        if line.strip() == "":
            continue
        else:
            content_list.append(line.strip())
    print(content_list)
    return lines