import os
import csv
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from sentence_transformers import SentenceTransformer

path = os.getcwd()
target = 'Training-Set-2018/'
if not os.path.exists(target + 'FilterSent'):
    os.makedirs(target + 'FilterSent')

entries = os.listdir(target)
model = SentenceTransformer('bert-base-nli-mean-tokens')


def Sort_Tuple1(tup):
    return (sorted(tup, key=lambda x: x[0]))


def maxn(list1, N):
    final_list = []

    for i in range(0, N):
        max1 = (0, 0, '')

        for j in range(len(list1)):
            if list1[j][0] > max1[0]:
                max1 = list1[j];

        list1.remove(max1);
        final_list.append(max1)

    return final_list


for entry in entries:
    if entry == 'FilterSent':
        continue
    temPath = path + '/' + target + entry
    count = 0
    refPath = glob.glob(temPath + '/Reference_XML/' + '*.csv')[0]
    annPath = glob.glob(temPath + '/annotation/' + '*.csv')[0]
    filename = refPath.split('/')[-1]
    outpath = target + 'FilterSent/' + filename
    df1 = pd.read_csv(annPath)
    df2 = pd.read_csv(refPath)

    with open(outpath, 'w', newline='') as f:
        thewriter = csv.writer(f)
        listRow = ['id', 'sentence']
        thewriter.writerow(listRow)
        finalresult = list()

        for cnt, line in df1.iterrows():
            # f5.write(str(cnt))
            list1 = list()
            list1.append(line['sentence'].lower())
            result = list()
            # df2 = pd.read_csv(filepath)
            for cnt1, line1 in df2.iterrows():
                # start  =  time()
                list2 = list()
                tu = (line1['id'], line1['sentence'])
                list2.append(line1['sentence'].lower())
                v1 = model.encode(list1)
                v2 = model.encode(list2)
                distance = cosine_similarity(v1, v2)
                tu = (distance[0][0], line1['id'], line1["sentence"])
                result.append(tu)
                print("-----------------------------------------")
            result = maxn(result, 5)
            for element in result:
                finalresult.append(element[1:])
            print(result)
        print(len(finalresult))
        finalresult1 = Sort_Tuple1(set(finalresult))
        for line3 in finalresult1:
            thewriter.writerow([line3[0], str(line3[1])])

















