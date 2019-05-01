#Create single .txt file from all .txt files contained in a directory
#Use to create single file from data in directories prior to further processing

import sys, os, io

directory = sys.argv[1]

out_name = sys.argv[2]
outfile = io.open(sys.argv[2], encoding = "utf-8", mode = "w+")

for filename in os.listdir(directory):
  if filename.endswith(".txt") and out_name not in filename:
    f = io.open(filename, encoding = "utf-8")
    lines = f.read()
    outfile.write(lines)
    outfile.write('\n')
  else:
    continue
