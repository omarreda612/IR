import nltk
from nltk import word_tokenize
word = input('enter your word : ')
word_list = []
file_names = [r"C:\Users\Admin\Documents\cis\level3\IR\section\task1\doc1.txt",r"C:\Users\Admin\Documents\cis\level3\IR\section\task1\doc2.txt",r"C:\Users\Admin\Documents\cis\level3\IR\section\task1\doc3.txt",r"C:\Users\Admin\Documents\cis\level3\IR\section\task1\doc4.txt"]
for file in file_names:
    with open (file, 'r') as f :
        word_list.append(word_tokenize(f.read()))

for i in range(len(word_list)):
    for j in range(len(word_list[i])):
        if word == word_list[i][j]:
            print("(",i+1,")",end=" ")
            break
         
