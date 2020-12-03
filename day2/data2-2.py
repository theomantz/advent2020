
# As a Python novice, i feel its best to complete these challenges without importing libraries
# What i've done here is solve these problems as best as i can with the standard tools that i know how to use

def parsed_password_data(data_file):
    
    # initializing the variables / data stores for the problem
    # there are several, most being intermediate variables

    int_imp = ''
    int_imp_range = []
    string_support = ''
    letter_carrier = ''
    data_store = []
    data_store_ultimate = []

    with open(data_file, 'r') as data:
        for itr in data:

            # to parse through the data i sliced through the strings using intermediate steps to remove unnessary values
            # naming convention was arbitrary at first but a more standard system was easier to keep track of

            int_imp += itr[:itr.find(' ')] 
            int_imp_range.append(int(int_imp[ : int_imp.find('-')]))
            int_imp_range.append(int(int_imp[int_imp.find('-') + 1 : ]))
            string_support += itr[itr.find(' ') + 1: -1 ]
            letter_carrier  += string_support[:1]
            string_support = string_support[3:]

            # using an intermediary data storage variable to format the data how i would like for ultimate result

            data_store.append(int_imp_range)
            data_store.append(letter_carrier)
            data_store.append(string_support)

            data_store_ultimate.append(data_store)

            # clearing out the intermediate variables for further iterations

            int_imp = ''
            int_imp_range = []
            string_support = ''
            letter_carrier = ''
            data_store = []            

            # returning the 'ultimate' list

        return data_store_ultimate

def passing_passwords_2(parsed_password_data):
    
    # intializing storage variables

    x = []
    y = ''
    z = ''
    l_index = 0
    u_index = 0
    count = 0
    passed = 0

    for itr in parsed_password_data:
        x, y, z = itr
        l_index = min(x) - 1 
        u_index = max(x) - 1
        if z[l_index] == y and z[u_index] != y:
            passed += 1
        elif z[l_index] != y and z[u_index] == y:
            passed += 1
    return print(passed)
                
passing_passwords_2(parsed_password_data('data2.txt'))