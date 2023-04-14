from nltk import word_tokenize
from nltk import sent_tokenize

text = input('enter your text :')
choice = int(input('select choice : '))

if choice == 1:
     print(word_tokenize(text))
elif choice == 2:
     print(sent_tokenize(text))
else:
     print(text)

