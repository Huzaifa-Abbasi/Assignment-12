'''Write a program that reads a sentence and counts the number of times each word appears. Use 
a dictionary to store the word counts.'''

sentence = input("Enter a sentence ")
words = sentence.split()

dict = {}
for word in words:

    if word in dict:
        dict[word] +=1

    else:
        dict[word] =1
    
print(dict)
