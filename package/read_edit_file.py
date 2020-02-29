import re

def read_count_seq (wordsSplit):
    return string_count(wordsSplit)

def read_count_MapR(p, number_of_process, file_detail):
    subSize = int(len(file_detail) / number_of_process)
    results = []
    for i in range(number_of_process):
        initial = int(i * subSize)
        if i == number_of_process - 1:
            end = len(file_detail)
        else:
            end = int((i + 1) * subSize)
        handle = p.apply_async(string_count,([file_detail[initial:end]]))
        results.append(handle)
    word_tracking_mapR = {}
    for r in results:
        d = r.get()
        for key in d:
            if key in word_tracking_mapR:
                word_tracking_mapR [key] = word_tracking_mapR[key] + d[key]
            else:
                word_tracking_mapR [key] = d [key]

    return word_tracking_mapR

def split_file(file_name):
    with open(file_name, 'r', encoding='UTF-8') as f:
        file_detail = f.read().split()
        f.close()
    return file_detail

def string_count(word_list):
    word_tracking = {}
    
    for w in word_list:
        w = re.sub(r"[^a-zA-Z0-9]",'', w)

        if w == '' or not w[0].isupper():
            continue
        elif w not in word_tracking:
            word_tracking[w] = 1
        else:
            word_tracking[w] += 1
    return word_tracking

