#UC Davis Computational Linguistics Lab
#Author: Sam Davidson

#Simple script to calculate Krippendorff's Alpha from a csv indicating annotation agreements
#Input file(s) is the comparison_union csv file output by the agreement_by_union.py script
#You may list as many input csvs as you like in the command line arguments
#Dependencies: krippendorff python package

import io, sys, krippendorff


a1=[]
a2=[]

for infile in sys.argv[1:]:
  for line in io.open(infile):
    split = line.split(',')
    a1pos = int(split[0])
    a2pos = int(split[1])
    a1.append(a1pos)
    a2.append(a2pos)

data=[a1,a2]

print(krippendorff.alpha(data))
