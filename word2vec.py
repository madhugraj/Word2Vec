from nltk.tokenize import sent_tokenize, word_tokenize 
import warnings 

warnings.filterwarnings(action = 'ignore') 

import gensim 
from gensim.models import Word2Vec

sample = open("path", "r") 
s = sample.read() 
f = s.replace("\n", " ") 
  
data = [] 
  
 # iterate through each sentence in the file 
for i in sent_tokenize(f): 
    for j in word_tokenize(i): 
        temp.append(j.lower()) 
    data.append(temp) 
    
model1 = gensim.models.Word2Vec(data, min_count = 1,size = 100, window = 5) 
model2 = gensim.models.Word2Vec(data, min_count = 1, size = 100,window = 5, sg = 1) 

print("Cosine similarity between 'Debit ' " +"and Credit Card Receipts' - CBOW : ", model1.similarity('x', 'y'))
