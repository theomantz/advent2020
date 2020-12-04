def toboggan_tree_count(data_file, right, down):

    tree_line_list = []
    
    #opening, reading, and parsing the txt file to a more usable format
    #chosen here was a list with each tree line as a string
    #this will allow for continutity as the tree lines 'run out'    towards the edge

    with open(data_file, 'r') as data:
        for itr in data:
            tree_line_list.append(itr[:-1])
    itr = ''
    i = 0
    tree_counter = 0
    down_acc = 0
    right_acc = 0
    itr = 0 
    last_row_index = len(tree_line_list) - 1

    while i <= last_row_index:
        itr = tree_line_list[down_acc]
        if right_acc >= len(itr):
            right_acc = right_acc - len(itr)
        if itr[right_acc] == '#':
            tree_counter += 1

        right_acc = right_acc + right
        down_acc = down_acc + down
        i += down
    return tree_counter

'''
first = toboggan_tree_count('data3.txt', 1, 1)
print(first, '\n')
second = toboggan_tree_count('data3.txt', 3, 1)
print(second, '\n')
third = toboggan_tree_count('data3.txt', 5, 1)
print(third, '\n')
fourth = toboggan_tree_count('data3.txt', 7, 1)
print(fourth, '\n')
fifth = toboggan_tree_count('data3.txt', 1, 2)
print(fifth, '\n')
'''
    

product = (toboggan_tree_count('data3.txt', 1, 1) * toboggan_tree_count('data3.txt', 3, 1) * toboggan_tree_count('data3.txt', 5, 1) 
            * toboggan_tree_count('data3.txt', 7, 1) * toboggan_tree_count('data3.txt', 1, 2)) 

print(product)