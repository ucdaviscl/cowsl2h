#Remove extraneous whitespace and quotation marks from texts prior to processing

import io, sys

outfile = io.open(sys.argv[1][:-3] + "clean2.txt", mode="w+", encoding='utf-8')

with io.open(sys.argv[1], encoding='utf-8') as infile:
  for line in infile:
    if line.strip() == '' or line.strip() == '\"':
      continue
    else:
      outfile.write(line.strip().strip('\"') + '\n')
