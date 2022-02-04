def update_Courier_list (): 
    Courier_list = display('Courier.txt')
    Courier_index= int(input('enter the index of the Courier:'))
    new_Courier_name=input('enter another Courier:')
    Courier_list[Courier_index] = new_Courier_name + '\n'

    with open('Courier.txt', 'w') as file:
	    file.writelines(Courier_list)



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