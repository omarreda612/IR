from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.stem import PorterStemmer  
from nltk.stem.snowball import SnowballStemmer as ss
ps = PorterStemmer()
snow_stemmer = ss(language='english')

print('Choice number 1: print tokenized words \nChoice number 2: print tokenized sentences\nChoice number 3: print original text\nChoice number 4: stemming')
text = input('enter your text :')
choice = int(input('select choice : '))

if choice == 1:
     print(word_tokenize(text))
elif choice == 2:
     print(sent_tokenize(text))
elif choice == 3:
     print(text)
elif choice == 4:
     word = int(input('choose wich stemmer prefer : porter(1) or snowball(2) : '))
     if word == 1:
          print(ps.stem(text))
     elif word == 2:
          print(snow_stemmer.stem(text))

