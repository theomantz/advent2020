def readfile(data_file):
    data_lst = []
    with open(data_file, 'r') as passport_data:
        for data in passport_data.read().split('\n\n'):
            data_lst.append(data.replace('\n', ' '))
    return data_lst

def entry_string(input_data):
    lst_return = []
    for data in input_data.split(' '):
        lst_return.append(data)
    return lst_return

def field_return(lst_item):
    field_lst = []; lst = []; lst = lst_item.split(':')
    field_lst.append(lst[0])
    for itm in lst[1:-1]:
        field_lst.append(itm[-3:])
    return field_lst

def req_fields(field_lst):
    req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    check = all(item in field_lst for item in req)
    return check

def field_check(list_items):
    for i in list_items:
        field = i[0:3]
        val = i[4:]
        if field == 'byr':
            if len(val) != 4:
                return False
            val = int(val)
            if val < 1920 or val > 2002:
                return False
        elif field == 'iyr': 
            if len(val) != 4:
                return False
            val = int(val)
            if val < 2010 or val > 2020:
                return False
        elif field == 'eyr':
            if len(val) != 4:
                return False
            val = int(val)
            if val < 2020 or val > 2030:
                return False
        elif field == 'hgt':
            if val.find('in') != -1:
                units = 'in'
                val = int(val.strip(units))
                if val < 59 or val > 76:
                    return False
            elif val.find('cm') != -1:
                units = 'cm'
                val = int(val.strip(units))
                if val < 150 or val > 193:
                    return False
            else:
                return False
        elif field == 'hcl':
            if val[0] != '#':
                return False
            val = val[1:]
            k = ['a', 'b', 'c', 'd', 'e', 'f']
            for i in range(10):
                i = str(i)
                k.append(i)
            for i in val:
                if i not in k:
                    return False
        elif field == 'ecl':
            acc_ecl = ['amb', 'brn', 'blu', 'gry', 'grn', 'hzl', 'oth']
            if val not in acc_ecl:
                return False
        elif field == 'pid':
            if len(val) != 9:
                return False
    return True

if __name__ == "__main__":
    input = readfile('passport_data.txt')
    counter = 0
    for entry in input:
        fields = field_return(entry)
        lst_entry = entry_string(entry)
        if req_fields(fields) == True:
            if field_check(lst_entry) == True:
                counter += 1
    print(counter)

