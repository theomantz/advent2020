
#Step 1 import and parse range values from data in text file 'data2.txt'

def parse_range(data_file):
    char_range_list = []
    data_list = []
    #counter = 0
    with open(data_file, 'r') as data:
        for itr in data:
            data_list.append(itr[:-1])
            # print(data_list)
            char_range = []
            for xtr in list.index(data_list, 0):
                char_range.append(data_list[xtr])
                print(char_range)
                
parse_range('data2.txt')