#Sequences (Lists/Tuples):

#Question 2: Write a function remove_duplicates(sequence) that takes a 
#sequence (list or tuple) and returns a new sequence with duplicates 
#removed while maintaining the original order of elements. 

#sample input = 
#input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
#result = remove_duplicates(input_sequence)
#print(result)  # Output: [2, 3, 4, 5, 6, 7]

def remove_duplicates(sequence):
    new_list = []
    for x in sequence:
        if x not in new_list:
            new_list.append(x)
    if type(sequence) == tuple:
        return print(tuple(new_list))
    else:
        return print(new_list)

remove_duplicates((2, 3, 2, 4, 5, 3, 6, 7, 5))