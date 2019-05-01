#UC Davis Computational Linguistics Lab
#Author: Sam Davidson

#Simple script to align senteces from two annotators into a single parallel file for
#inter-annotator agreement calculation.

#Usage: python3 prep_union.py file1.txt file2.txt
#Note: files should be preprocessed using preprocess.py if they contain extraneous whitespace

import nltk
from nltk.tokenize import RegexpTokenizer
import io
import sys
#from itertools import izip

tokenizer = RegexpTokenizer('\w+|[\[[a-z]*\]{[a-z]*}<\S*>|\S+')

with io.open(sys.argv[1], mode='r', encoding='utf-8') as infile:
  with io.open(sys.argv[2], mode='r', encoding='utf-8') as infile2:  
    with io.open(sys.argv[3], mode='w+', encoding='utf-8') as outfile:
      for line_1, line_2 in zip(infile, infile2):
        sents1 = nltk.tokenize.sent_tokenize(line_1)
        sents2 = nltk.tokenize.sent_tokenize(line_2)
        for sent1, sent2 in zip(sents1,sents2):
          tokens1 = tokenizer.tokenize(sent1)
          tokens2 = tokenizer.tokenize(sent2)
          sent1 = ' '.join(tokens1).strip().strip('\"')
          sent2 = ' '.join(tokens2).strip().strip('\"')
          if sent1 != '':
            outfile.write(sent1.encode('utf-8').decode('utf-8')) 
            outfile.write(u" ||| ")
            outfile.write(sent2.encode('utf-8').decode('utf-8'))
            outfile.write(u'\n')

         
