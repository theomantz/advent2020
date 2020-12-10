def readfile(data_file):
    data_lst = []
    with open(data_file, 'r') as passport_data:
        for data in passport_data.read().split('\n\n'):
            data_lst.append(data.replace('\n', ' '))
    return data_lst

def field_return(lst_item):
    field_lst = []
    lst = []
    lst = lst_item.split(':')
    field_lst.append(lst[0])
    for itm in lst[1:-1]:
        field_lst.append(itm[-3:]) 
        field_lst = sorted(field_lst)
    return field_lst

def req_fields(field_lst):
    req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    check = all(item in field_lst for item in req)
    return check

def counter_funct(check):
    counter = 0
    if check == True:
        counter += 1
    

if __name__ == "__main__":
    input = readfile('passport_data.txt')
    counter = 0
    for entry in input:
        fields = field_return(entry)
        check = req_fields(fields)
        if check == True:
            counter += 1
    print(counter)
