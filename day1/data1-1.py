

x = []

with open('data.txt', 'r') as data:
    for itr in data:
        itr_proper = int(itr[:-1])
        x.append(itr_proper)
    # print(x)

i = 0
j = 0

while i + j != 2020:
    for i in x:
        for j in x:
            if i + j == 2020:
                print(i * j)
            