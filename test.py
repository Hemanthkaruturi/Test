import nltk
import re
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
test = "I am also changing this. Let see what happens"
text = "Hey i am just testing the git"
text = str(object=text)
text = re.sub('[^\w\s]','', text)
text = word_tokenize(text)
print(text)
print(text)
tags = nltk.pos_tag(text)
print(tags)
