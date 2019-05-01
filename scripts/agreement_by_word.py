#UC Davis Computational Linguistics Lab
#Author: Sam Davidson

#Script to caluclate Cohen's Kappa for agreement with every token considered an annotation position
#Outputs csv file to be used in calculating Krippendorff's Alpha

#Input file is " ||| " separated parallel sentences ouput by prep_union.py script

import sys, re, io, string

regex = re.compile(r'\[[a-z]*\]{[a-z]*}<\S*>')
total = 0
disagree = 0
agree = 0
annotator0 = [0,0]
annotator1 = [0,0]
annotation_list = []

outfile = io.open(sys.argv[1][:-3] + 'comparison_word.csv', mode='w+', encoding='utf-8')

with io.open(sys.argv[1], encoding="utf-8") as infile:
  for line in infile:
    
    total += 1
    sents = line.split(' ||| ')
    toklist0 = sents[0].split()
    toklist1 = sents[1].split()
    
    for tok0, tok1 in zip(toklist0, toklist1):
      if tok0 not in string.punctuation:
        match_triple = (total - 1, tok0, tok1)
        annotation_list.append(match_triple)

for match_triple in annotation_list:
  
  if regex.search(match_triple[1]):
    annotator0[1] += 1
    out0 = 1
  else:
    annotator0[0] += 1
    out0 = 0

  if regex.search(match_triple[2]):
    annotator1[1] += 1
    out1 = 1
  else:
    annotator1[0] += 1
    out1 = 0

#  if match_triple[1] == match_triple[2]:
  if out0 == out1:
    agree += 1
  else:
    disagree += 1

  outfile.write(str(out0) + ',' + str(out1) + '\n')      

total = len(annotation_list)

agreement = agree/total
p_no_annotation = (annotator0[0]/(total)) * (annotator1[0]/(total))
print('p_no_annotation: ', p_no_annotation)
p_annotation = (annotator0[1]/(total)) * (annotator1[1]/(total))
print('p_annotation: ', p_annotation)
p_e = p_no_annotation + p_annotation 
k = (agreement-p_e)/(1-p_e)
     
print("agreements: ", agree)
print('disagreements: ', disagree)
print("agreement: ", agreement)
print("p_e: ", p_e)
print("k: ", k)   
