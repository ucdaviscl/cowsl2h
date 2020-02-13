import pickle
import os, sys, glob, io



def create_metadata_dict(directory):
    file_list = [filename for filename in glob.iglob(directory + '/**', recursive=True)]
    out_dict = dict()
    for filename in file_list:
        if os.path.isfile(filename) and "metadata.txt" in filename:
            id = filename.split('/')[-1].split('.')[0]
            quarter = filename.split('/')[-3]
            with open(filename) as input:
                metadata = input.readlines()[0].strip().split("|||")
                out_dict[id][quarter] = metadata
    return out_dict

if __name__ == "__main__":
    meta_dict = create_metadata_dict(sys.argv[1])

    tagged_data = pickle.load(io.open(sys.argv[2], mode="rb"))

    out_list = list()

    for item in tagged_data:
        id = item[0]
        quarter = item[1]
        tagged_text = item[2]
        metadata = meta_dict[id][quarter]
        level = int(metadata[0][4:]) if (metadata[0] not in "") else 0
        out_tuple = (id, quarter, level, tagged_text)
        print(out_tuple)
        out_list.append(out_tuple)

    out_pickle = io.open(sys.argv[3], mode="wb")

    pickle.dump(out_list, out_pickle)
