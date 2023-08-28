#Dictionaries: 

#Question 3: Implement a function word_frequency(sentence) that takes 
#a sentence and returns a dictionary containing the frequency of each 
#word in the sentence. 

#Ignore punctuation and consider words in a case-insensitive manner.

#sample input = 
#sentence = "This is a test sentence. This sentence is a test."
#result = word_frequency(sentence)
#print(result)

def word_frequency(sentence):
    new_sentence = sentence.translate({ord(i): None for i in '.?!,:;"\'/-()[]\\'})
    my_list = new_sentence.split()
    my_dict = {}
    for word in my_list:
        if (my_dict.__contains__(word)):
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    return print(my_dict)

word_frequency("This is a test sentence. This sentence is a test.")