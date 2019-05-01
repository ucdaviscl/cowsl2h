#UC Davis Computational Linguistics Lab
#Author: Sam Davidson

#Script to calculate Cohen's Kappa and output file for use in Krippendorff's Alpha calculation

#Usage: Input file is a file containing parallel sentences from two annotators, separated by " ||| "
# This input file can be created from two files containing the individual annotators sentences
# using the prep_union.py script.
# python3 agreement_by_union.py input_parallel_file.txt 

import sys, re, io

#pattern to locate annotations
regex = re.compile(r'\[[a-z]*\]{[a-z]*}<\S*>')

total = 0
disagree = 0
agree = 0
annotator0 = [0,0]
annotator1 = [0,0]
annotation_list = []


#outfile1 will be a csv with a single line for each annotation indicating if annotators agree
outfile = io.open(sys.argv[1][:-3] + 'comparison_union.csv', mode='w+', encoding='utf-8')

#a paired sentence list of annotations
outfile2 = io.open(sys.argv[1][:-3] + 'annotations.txt', mode='w+', encoding='utf-8')

#a paired sentence list of disagreements
outfile3 = io.open(sys.argv[1][:-3] + 'disagreements.txt', mode='w+', encoding='utf-8')

with io.open(sys.argv[1], encoding="utf-8") as infile:
  for line in infile:
    
    total += 1
    sents = line.split(' ||| ')
    toklist0 = sents[0].split()
    toklist1 = sents[1].split()
    
    for tok0, tok1 in zip(toklist0, toklist1):
      if regex.search(tok0) or regex.search(tok1):
        match_triple = (total - 1, tok0, tok1)
        annotation_list.append(match_triple)
        outfile2.write(str(total))
        outfile2.write('   ')
        outfile2.write(line)
        outfile2.write('\n')
      if (regex.search(tok0) and not(regex.search(tok1))) or (not(regex.search(tok0)) and regex.search(tok1)):
        outfile3.write(str(total))
        outfile3.write('   ')
        outfile3.write(line)
        outfile3.write('\n')

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
  if out0 == 1 and out1 == 1:
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
p_e = p_no_annotation + p_annotation #p_e for calculation of k
k = (agreement-p_e)/(1-p_e) #Cohen's Kappa
     
print("agreements: ", agree)
print('disagreements: ', disagree)
print("agreement: ", agreement)
print("p_e: ", p_e)
print("k: ", k)   
