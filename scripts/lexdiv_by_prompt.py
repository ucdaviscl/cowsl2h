import csv, io, nltk
from collections import defaultdict
from matplotlib import pyplot
import lexical_diversity as lexdiv

essays = list()
essays_special = list()
essays_terrible = list()

def create_essay_list(directory):
    file_list = [filename for filename in glob.iglob(directory + '/**', recursive=True)]
    for filename in file_list:
        if os.path.isfile(filename) and "id.txt" not in filename and "metadata" not in filename:
            id = filename.split('/')[-1][:-4]
            with open(filename) as essay:
                text = essay.readlines()
                processed_text = [line.strip() for line in text]
                out_text = ' '.join(processed_text)
                if len(out_text.split()) >= 50:
                    if "special" in filename:
                        essays_special.append((id, out_text))
                    elif "terrible" in filename:
                        essays_terrible.append((id, out_text))

totals = defaultdict()
totals_famous = defaultdict()
totals_vacation = defaultdict()
class_count = defaultdict()
class_count_famous = defaultdict()
class_count_vacation = defaultdict()

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

for essay in essays_famous:
  if(essay[0] not in totals_famous):
    if essay[1] > 0:
      totals_famous[essay[0]] = essay[1]
  else:
    if essay[1] > 0:
      totals_famous[essay[0]] += essay[1]
  if (essay[0] not in class_count_famous):
    if essay[1] > 0:
      class_count_famous[essay[0]] = 1
  else:
    if essay[1] > 0:
      class_count_famous[essay[0]] += 1

for essay in essays_vacation:
  if(essay[0] not in totals_vacation):
    if essay[1] > 0:
      totals_vacation[essay[0]] = essay[1]
  else:
    if essay[1] > 0:
      totals_vacation[essay[0]] += essay[1]
  if (essay[0] not in class_count_vacation):
    if essay[1] > 0:
      class_count_vacation[essay[0]] = 1
  else:
    if essay[1] > 0:
      class_count_vacation[essay[0]] += 1

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

SPA1_famous = totals_famous[1]/class_count_famous[1]
SPA2_famous = totals_famous[2]/class_count_famous[2]
SPA3_famous = totals_famous[3]/class_count_famous[3]
SPA21_famous = totals_famous[21]/class_count_famous[21]
SPA22_famous = totals_famous[22]/class_count_famous[22]
SPA23_famous = totals_famous[23]/class_count_famous[23]
SPA24_famous = totals_famous[24]/class_count_famous[24]
SPA31_famous = totals_famous[31]/class_count_famous[31]
SPA32_famous = totals_famous[32]/class_count_famous[32]
SPA33_famous = totals_famous[33]/class_count_famous[33]

SPA1_vacation = totals_vacation[1]/class_count_vacation[1]
SPA2_vacation = totals_vacation[2]/class_count_vacation[2]
SPA3_vacation = totals_vacation[3]/class_count_vacation[3]
SPA21_vacation = totals_vacation[21]/class_count_vacation[21]
SPA22_vacation = totals_vacation[22]/class_count_vacation[22]
SPA23_vacation = totals_vacation[23]/class_count_vacation[23]
SPA24_vacation = totals_vacation[24]/class_count_vacation[24]
SPA31_vacation = totals_vacation[31]/class_count_vacation[31]
SPA32_vacation = totals_vacation[32]/class_count_vacation[32]
SPA33_vacation = totals_vacation[33]/class_count_vacation[33]

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

print("SPA1_famous lexdiv: " + str(SPA1_famous))
print("SPA2_famous lexdiv: " + str(SPA2_famous))
print("SPA3_famous Avg lexdiv: " + str(SPA3_famous))
print("SPA21_famous Avg lexdiv: " + str(SPA21_famous))
print("SPA22_famous Avg lexdiv: " + str(SPA22_famous))
print("SPA23_famous Avg lexdiv: " + str(SPA23_famous))
print("SPA24_famous Avg lexdiv: " + str(SPA24_famous))
print("SPA31_famous Avg lexdiv: " + str(SPA31_famous))
print("SPA32_famous Avg lexdiv: " + str(SPA32_famous))
print("SPA33_famous Avg lexdiv: " + str(SPA33_famous))

print()

print("SPA1_vacation Avg lexdiv: " + str(SPA1_vacation))
print("SPA2_vacation Avg lexdiv: " + str(SPA2_vacation))
print("SPA3_vacation Avg lexdiv: " + str(SPA3_vacation))
print("SPA21_vacation Avg lexdiv: " + str(SPA21_vacation))
print("SPA22_vacation Avg lexdiv: " + str(SPA22_vacation))
print("SPA23_vacation Avg lexdiv: " + str(SPA23_vacation))
print("SPA24_vacation Avg lexdiv: " + str(SPA24_vacation))
print("SPA31_vacation Avg lexdiv: " + str(SPA31_vacation))
print("SPA32_vacation Avg lexdiv: " + str(SPA32_vacation))
print("SPA33_vacation Avg lexdiv: " + str(SPA33_vacation))

x = list()
y = list()

# for essay in essays:
#   x.append(essay[0])
#   y.append(essay[1])

x = [SPA1, SPA2, SPA3, SPA21, SPA22, SPA23,SPA24]
y = ["SPA1", "SPA2", "SPA3", "SPA21", "SPA22", "SPA23","SPA24"]
w = [SPA31, SPA32, SPA33]
z = ["SPA31", "SPA32", "SPA33"]

a = [SPA1_famous, SPA2_famous, SPA3_famous, SPA21_famous, SPA22_famous, SPA23_famous, SPA24_famous]
b = [SPA1_vacation, SPA2_vacation, SPA3_vacation, SPA21_vacation, SPA22_vacation, SPA23_vacation, SPA24_vacation]
c = [SPA31_famous, SPA32_famous, SPA33_famous]
d = [SPA31_vacation, SPA32_vacation, SPA33_vacation]

pyplot.title("Lexical Diversity by Prompt")
pyplot.ylabel("MTLD Score")
pyplot.xlabel("Course Number")
#pyplot.plot(y, x, 'bo-') #this is a scatterplat, using green(g) triangles(^)
#pyplot.plot(z, w, 'r+-')
pyplot.plot(y, a, 'bo-', label = "Famous prompt") #this is a scatterplat, using green(g) triangles(^)
pyplot.plot(y, b, 'r+-', label = "Vacation prompt")
pyplot.plot(z, c, 'bo-')
pyplot.plot(z, d, 'r+-')
pyplot.legend()
pyplot.show() #display graph
