def return_list(filename):

    Courier_list = []

    fo = open(filename, "r")
    lines = fo.readlines()
    for line in lines:
        if line.strip() == "":
            continue
        else:
            Courier_list.append(line.strip())
    
    return Courier_list




