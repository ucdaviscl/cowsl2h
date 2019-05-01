#UC Davis Computational Linguistics Lab
#Author: Sam Davidson

#Script to calculate precision, recall, F1 and F0.5 given a
#csv containing agreement information as output by agreement_by_union.py

#Usage: python3 precision_recall.py input.csv
#Note: can take any N>0 number of files as input

import io, sys

match = 0
true_annotations = 0
test_annotations = 0

for file_in in sys.argv[1:]:
  with io.open(file_in) as infile:
    for line in infile:
      data = line.split(',')
      true = int(data[0])
      test = int(data[1].strip())
      if true == 1:
        true_annotations += 1
      if test == 1:
        test_annotations += 1
      if true == 1 and test == 1:
        match += 1


precision = match/test_annotations
recall = match/true_annotations
F1 = (2 * precision * recall)/(recall + precision)
F05 = (1.25 * recall * precision)/(recall + (.25*precision))


print("True annotations: ", true_annotations)
print("Test annotations: ", test_annotations)
print("Precision: ", precision)
print("Recall: ", recall)
print("F1: ", F1)
print("F05: ", F05)

    
