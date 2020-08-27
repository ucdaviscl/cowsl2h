import pyfreeling as freeling
import sys, io, glob, os
import string
import pickle

essays = list()
essays_tagged = list()
essays_vacation = list()
essays_vacation_tagged = list()
essays_famous = list()
essays_famous_tagged = list()

## -----------------------------------------------
## Do whatever is needed with analyzed sentences
## -----------------------------------------------
def ProcessSentences(ls):
    result_list = list()

    # for each sentence in list
    for s in ls :
        sent_list = list()
        # for each word in sentence
        for w in s :
#            if w.get_lemma() not in string.punctuation:
            word_tuple = (w.get_form().lower(), w.get_lemma(), w.get_tag())
            sent_list.append(word_tuple)

        result_list.append(sent_list)

#    print(result_list)
    return result_list


## ------------  output a parse tree ------------
def printTree(ptree, depth):

    node = ptree.begin();

    print(''.rjust(depth*2),end='');
    info = node.get_info();
    if (info.is_head()): print('+',end='');

    nch = node.num_children();
    if (nch == 0) :
        w = info.get_word();
        print ('({0} {1} {2})'.format(w.get_form(), w.get_lemma(), w.get_tag()),end='');

    else :
        print('{0}_['.format(info.get_label()));

        for i in range(nch) :
            child = node.nth_child_ref(i);
            printTree(child, depth+1);

        print(''.rjust(depth*2),end='');
        print(']',end='');

    print('');

## ------------  output a parse tree ------------
def printDepTree(dtree, depth):

    node = dtree.begin()

    print(''.rjust(depth*2),end='');

    info = node.get_info();
    link = info.get_link();
    linfo = link.get_info();
    print ('{0}/{1}/'.format(link.get_info().get_label(), info.get_label()),end='');

    w = node.get_info().get_word();
    print ('({0} {1} {2})'.format(w.get_form(), w.get_lemma(), w.get_tag()),end='');

    nch = node.num_children();
    if (nch > 0) :
        print(' [');

        for i in range(nch) :
            d = node.nth_child_ref(i);
            if (not d.begin().get_info().is_chunk()) :
                printDepTree(d, depth+1);

        ch = {};
        for i in range(nch) :
            d = node.nth_child_ref(i);
            if (d.begin().get_info().is_chunk()) :
                ch[d.begin().get_info().get_chunk_ord()] = d;

        for i in sorted(ch.keys()) :
            printDepTree(ch[i], depth + 1);

        print(''.rjust(depth*2),end='');
        print(']',end='');

    print('');

## ----------------------------------------------
## -------------    MAIN PROGRAM  ---------------
## ----------------------------------------------

## Check whether we know where to find FreeLing data files
if "FREELINGDIR" not in os.environ :
   if sys.platform == "win32" or sys.platform == "win64" : os.environ["FREELINGDIR"] = "C:\\Program Files"
   else : os.environ["FREELINGDIR"] = "/usr/local"
   print("FREELINGDIR environment variable not defined, trying ", os.environ["FREELINGDIR"], file=sys.stderr)

if not os.path.exists(os.environ["FREELINGDIR"]+"/share/freeling") :
   print("Folder",os.environ["FREELINGDIR"]+"/share/freeling",
         "not found.\nPlease set FREELINGDIR environment variable to FreeLing installation directory",
         file=sys.stderr)
   sys.exit(1)


# Location of FreeLing configuration files.
DATA = os.environ["FREELINGDIR"]+"/share/freeling/";

# set locale to an UTF8 compatible locale
freeling.util_init_locale("default");

# get requested language from arg1, or English if not provided
lang = "es"
LANG = "es"
op= freeling.maco_options(LANG);
op.set_data_files( "",
                   DATA + "common/punct.dat",
                   DATA + LANG + "/dicc.src",
                   DATA + LANG + "/afixos.dat",
                   "",
                   DATA + LANG + "/locucions.dat",
                   DATA + LANG + "/np.dat",
                   DATA + LANG + "/quantities.dat",
                   DATA + LANG + "/probabilitats.dat");

# get installation path to use from arg2, or use /usr/local if not provided
#ipath = "/usr/local/Cellar/freeling/4.0_4";
ipath = "/usr/local/";

# path to language data
lpath = ipath + "/share/freeling/" + lang + "/"

# create analyzers
tk=freeling.tokenizer(lpath+"tokenizer.dat");
sp=freeling.splitter(lpath+"splitter.dat");
sid=sp.open_session();
# create the analyzer with the required set of maco_options
morfo=freeling.maco(op);
#  then, (de)activate required modules
morfo.set_active_options (False,  # UserMap
                          True,  # NumbersDetection,
                          True,  # PunctuationDetection,
                          True,  # DatesDetection,
                          True,  # DictionarySearch,
                          True,  # AffixAnalysis,
                          False, # CompoundAnalysis,
                          True,  # RetokContractions,
                          True,  # MultiwordsDetection,
                          True,  # NERecognition,
                          False, # QuantitiesDetection,
                          True); # ProbabilityAssignment

# create tagger
tagger = freeling.hmm_tagger(lpath+"tagger.dat",True,2)

def process_file(essay_lst, x):
    index = 1
    for entry in essay_lst:
        # create tagger
        essay = entry[1]
        id = entry[0]
        tagger = freeling.hmm_tagger(lpath+"tagger.dat",True,2)

        # create sense annotator
        sen = freeling.senses(lpath+"senses.dat");

        # create sense disambiguator
        wsd = freeling.ukb(lpath+"ukb.dat");

        # create dependency parser
        parser = freeling.chart_parser(lpath+"/chunker/grammar-chunk.dat");
        dep = freeling.dep_txala(lpath+"/dep_txala/dependences.dat", parser.get_start_symbol())

        # tokenize input line into a list of words
        lw = tk.tokenize(essay)
        # split list of words in sentences, return list of sentences
        ls = sp.split(lw)

        # perform morphosyntactic analysis and disambiguation
        ls = morfo.analyze(ls)
        ls = tagger.analyze(ls)

        # annotate and disambiguate senses
        ls = sen.analyze(ls);
        ls = wsd.analyze(ls);
        # parse sentences
        ls = parser.analyze(ls);
        ls = dep.analyze(ls);

        # do whatever is needed with processed sentences
        if x == 2:
          essays_vacation_tagged.append((id, ProcessSentences(ls)))
        elif x == 3:
          essays_famous_tagged.append((id, ProcessSentences(ls)))
        print(index)
        index += 1

def create_essay_list(directory):
    file_list = [filename for filename in glob.iglob(directory + '/**', recursive=True)]
    for filename in file_list:
        if os.path.isfile(filename) and "id.txt" not in filename and "metadata" not in filename and "annotated" not in filename and "corrected" not in filename:
            id = filename.split('/')[-1].split('.')[0]
            quarter = filename.split('/')[-3]
            with open(filename) as essay:
                text = essay.readlines()
                processed_text = [line.strip() for line in text]
                out_text = ' '.join(processed_text)
                if len(out_text.split()) >= 50:
                    if "famous" in filename:
                        essays_famous.append((id, quarter, out_text))
                    elif "vacation" in filename:
                        essays_vacation.append((id, out_text))

directory = os.getcwd() + "/" + sys.argv[1]
#print(directory)
create_essay_list(directory)

#process_file(essays_vacation,2)
print("Num essays: ", len(essays_famous))
process_file(essays_famous,3)

#save the data sets to file for futher use
#pickle.dump(essays_vacation_tagged, open('essays_vacation_tagged_by_quarter.pickle', 'wb'))
pickle.dump(essays_famous_tagged, open('essays_famous_tagged_by_quarter.pickle', 'wb'))
