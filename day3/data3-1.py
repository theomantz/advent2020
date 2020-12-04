def toboggan_tree_count(data_file):

    tree_line_list = []
    #opening, reading, and parsing the txt file to a more usable format
    #chosen here was a list with each tree line as a string
    #this will allow for continutity as the tree lines 'run out' towards the edge

    with open(data_file, 'r') as data:
        for itr in data:
            tree_line_list.append(itr[:-1])
    
    tree_line_list = tree_line_list[1:]
    itr = ''
    right = 0
    tree_counter = 0

    for itr in tree_line_list:
        right += 3
        if right >= len(itr):
            right = right - len(itr)
        if itr[right] == '#':
            tree_counter += 1

    return print(tree_counter)



    

toboggan_tree_count('data3.txt')
