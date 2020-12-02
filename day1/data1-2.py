
def find_2020(data_file):
    x = []

    with open(data_file, 'r') as data:
        for itr in data:
            itr_proper = int(itr[:-1])
            x.append(itr_proper)

    i = 0
    j = 0


    for i in x:
        for j in x:
            for k in x:
                if i + j + k == 2020:
                    return i * j * k

find_2020('data.txt')
            