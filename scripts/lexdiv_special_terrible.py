import nltk, sys, glob, os
from collections import defaultdict
from matplotlib import pyplot
import lexical_diversity as lexdiv
from pos_tagging import align_metadata

#init lists to hold tuples of (id, text, mtld_score) for each essay
essays_special_init = list()
essays_terrible_init = list()

#iterate through files in data directory and create list of tuples with essay info
def create_essay_list(directory):
    file_list = [filename for filename in glob.iglob(directory + '/**', recursive=True)]
    for filename in file_list:
        if os.path.isfile(filename) and "id.txt" not in filename and "metadata" not in filename:
            id = filename.split('/')[-1][:-4]
            with open(filename) as essay:
                text = essay.readlines()
                processed_text = [line.strip() for line in text]
                out_text = ' '.join(processed_text)
                out_text = nltk.word_tokenize(out_text)
                if len(out_text) >= 50:
                    if "special" in filename:
                        #pass (level, mtld)
                        essays_special_init.append((id, out_text, lexdiv.mtld(out_text)))
                    elif "terrible" in filename:
                        essays_terrible_init.append((id, out_text, lexdiv.mtld(out_text)))

#Create metadata dict and essay list for special essay
#argv[1] is special directory
meta_dict_special = align_metadata.create_metadata_dict(sys.argv[1])
create_essay_list(sys.argv[1])
#Create metadata dict and essay list for terrible essay
#argv[2] is terrible directory
meta_dict_terrible = align_metadata.create_metadata_dict(sys.argv[2])
create_essay_list(sys.argv[2])

#init lists to hold paired (level, mtld) tuples
essays_special = list()
essays_terrible = list()

#pair the essay with level from mtld dict
#add to essay_special list
for essay in essays_special_init:
    level = 0
    if meta_dict_special[essay[0]][0][4:] not in ["", '\n']:
        level = int(meta_dict_special[essay[0]][0][4:])
    mtld = essay[2]
    essays_special.append((level, mtld))

#do the same for essay_terrible
for essay in essays_terrible_init:
    level = 0
    if meta_dict_terrible[essay[0]][0][4:] not in ["", '\n']:
        level = int(meta_dict_terrible[essay[0]][0][4:])
    mtld = essay[2]
    essays_terrible.append((level, mtld))

#put both together to create combined list
essays = essays_special + essays_terrible

#init dicts for totals by level
totals = defaultdict()
totals_special = defaultdict()
totals_terrible = defaultdict()
class_count = defaultdict()
class_count_special = defaultdict()
class_count_terrible = defaultdict()

#add up everything by level - sum mltd and keep track of num essays per level
for essay in essays:
  if(essay[0] not in totals):
    if essay[1] > 0:
      totals[essay[0]] = essay[1]
  else:
    if essay[1] > 0:
      totals[essay[0]] += essay[1]
  if (essay[0] not in class_count):
    if essay[1] > 0:
      class_count[essay[0]] = 1
  else:
    if essay[1] > 0:
      class_count[essay[0]] += 1

for essay in essays_special:
  if(essay[0] not in totals_special):
    if essay[1] > 0:
      totals_special[essay[0]] = essay[1]
  else:
    if essay[1] > 0:
      totals_special[essay[0]] += essay[1]
  if (essay[0] not in class_count_special):
    if essay[1] > 0:
      class_count_special[essay[0]] = 1
  else:
    if essay[1] > 0:
      class_count_special[essay[0]] += 1

for essay in essays_terrible:
  if(essay[0] not in totals_terrible):
    if essay[1] > 0:
      totals_terrible[essay[0]] = essay[1]
  else:
    if essay[1] > 0:
      totals_terrible[essay[0]] += essay[1]
  if (essay[0] not in class_count_terrible):
    if essay[1] > 0:
      class_count_terrible[essay[0]] = 1
  else:
    if essay[1] > 0:
      class_count_terrible[essay[0]] += 1

#calc avg mtld for each level
SPA1 = totals[1]/class_count[1]
SPA2 = totals[2]/class_count[2]
SPA3 = totals[3]/class_count[3]
SPA21 = totals[21]/class_count[21]
SPA22 = totals[22]/class_count[22]
SPA23 = totals[23]/class_count[23]
SPA24 = totals[24]/class_count[24]
SPA31 = totals[31]/class_count[31]
SPA32 = totals[32]/class_count[32]
SPA33 = totals[33]/class_count[33]

#same for special prompt
SPA1_special = totals_special[1]/class_count_special[1]
SPA2_special = totals_special[2]/class_count_special[2]
SPA3_special = totals_special[3]/class_count_special[3]
SPA21_special = totals_special[21]/class_count_special[21]
SPA22_special = totals_special[22]/class_count_special[22]
SPA23_special = totals_special[23]/class_count_special[23]
SPA24_special = totals_special[24]/class_count_special[24]
SPA31_special = totals_special[31]/class_count_special[31]
SPA32_special = totals_special[32]/class_count_special[32]
SPA33_special = totals_special[33]/class_count_special[33]

#same for terrible prompt
SPA1_terrible = totals_terrible[1]/class_count_terrible[1]
SPA2_terrible = totals_terrible[2]/class_count_terrible[2]
SPA3_terrible = totals_terrible[3]/class_count_terrible[3]
SPA21_terrible = totals_terrible[21]/class_count_terrible[21]
SPA22_terrible = totals_terrible[22]/class_count_terrible[22]
SPA23_terrible = totals_terrible[23]/class_count_terrible[23]
SPA24_terrible = totals_terrible[24]/class_count_terrible[24]
SPA31_terrible = totals_terrible[31]/class_count_terrible[31]
SPA32_terrible = totals_terrible[32]/class_count_terrible[32]
SPA33_terrible = totals_terrible[33]/class_count_terrible[33]

print("SPA1 Avg lexdiv: " + str(SPA1))
print("SPA2 Avg lexdiv: " + str(SPA2))
print("SPA3 Avg lexdiv: " + str(SPA3))
print("SPA21 Avg lexdiv: " + str(SPA21))
print("SPA22 Avg lexdiv: " + str(SPA22))
print("SPA23 Avg lexdiv: " + str(SPA23))
print("SPA24 Avg lexdiv: " + str(SPA24))
print("SPA31 Avg lexdiv: " + str(SPA31))
print("SPA32 Avg lexdiv: " + str(SPA32))
print("SPA33 Avg lexdiv: " + str(SPA33))

print()

print("SPA1_special lexdiv: " + str(SPA1_special))
print("SPA2_special lexdiv: " + str(SPA2_special))
print("SPA3_special Avg lexdiv: " + str(SPA3_special))
print("SPA21_special Avg lexdiv: " + str(SPA21_special))
print("SPA22_special Avg lexdiv: " + str(SPA22_special))
print("SPA23_special Avg lexdiv: " + str(SPA23_special))
print("SPA24_special Avg lexdiv: " + str(SPA24_special))
print("SPA31_special Avg lexdiv: " + str(SPA31_special))
print("SPA32_special Avg lexdiv: " + str(SPA32_special))
print("SPA33_special Avg lexdiv: " + str(SPA33_special))

print()

print("SPA1_terrible Avg lexdiv: " + str(SPA1_terrible))
print("SPA2_terrible Avg lexdiv: " + str(SPA2_terrible))
print("SPA3_terrible Avg lexdiv: " + str(SPA3_terrible))
print("SPA21_terrible Avg lexdiv: " + str(SPA21_terrible))
print("SPA22_terrible Avg lexdiv: " + str(SPA22_terrible))
print("SPA23_terrible Avg lexdiv: " + str(SPA23_terrible))
print("SPA24_terrible Avg lexdiv: " + str(SPA24_terrible))
print("SPA31_terrible Avg lexdiv: " + str(SPA31_terrible))
print("SPA32_terrible Avg lexdiv: " + str(SPA32_terrible))
print("SPA33_terrible Avg lexdiv: " + str(SPA33_terrible))

x = list()
y = list()

# for essay in essays:
#   x.append(essay[0])
#   y.append(essay[1])

x = [SPA1, SPA2, SPA3, SPA21, SPA22, SPA23,SPA24]
y = ["SPA1", "SPA2", "SPA3", "SPA21", "SPA22", "SPA23","SPA24"]
w = [SPA31, SPA32, SPA33]
z = ["SPA31", "SPA32", "SPA33"]

a = [SPA1_special, SPA2_special, SPA3_special, SPA21_special, SPA22_special, SPA23_special, SPA24_special]
b = [SPA1_terrible, SPA2_terrible, SPA3_terrible, SPA21_terrible, SPA22_terrible, SPA23_terrible, SPA24_terrible]
c = [SPA31_special, SPA32_special, SPA33_special]
d = [SPA31_terrible, SPA32_terrible, SPA33_terrible]

pyplot.title("Lexical Diversity by Prompt")
pyplot.ylabel("MTLD Score")
pyplot.xlabel("Course Number")
#pyplot.plot(y, x, 'bo-') #this is a scatterplat, using green(g) triangles(^)
#pyplot.plot(z, w, 'r+-')
pyplot.plot(y, a, 'bo-', label = "special prompt") #this is a scatterplat, using green(g) triangles(^)
pyplot.plot(y, b, 'r+-', label = "terrible prompt")
pyplot.plot(z, c, 'bo-')
pyplot.plot(z, d, 'r+-')
pyplot.legend()
pyplot.show() #display graph
