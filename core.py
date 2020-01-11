core.pyimport numpy as np 
import pandas as pd 
import json

newdf1 = pd.read_csv('data/dataset.csv')


def jaccard_similarity(query, document):
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection)/len(union)



for i in range(len(newdf1.iloc[:, 3].values)):
  newdf1.iloc[:, 3].values[i] = json.loads(newdf1.iloc[:, 3].values[i])


for i in range(len(newdf1.iloc[:, 4].values)):
  newdf1.iloc[:, 4].values[i] = json.loads(newdf1.iloc[:, 4].values[i])

def recommend(id):
  video_tags = []
  lim = 10
  v_limit = 0
  if len(id) > lim:
    v_limit =  lim
  else:
    v_limit = len(id)

  for i in range(v_limit):
    video_idx = list(newdf1.iloc[:, 0].values).index(id[i])
    video_tags = video_tags + newdf1.iloc[video_idx][3]

  similarity_vidoes_score = []
  
  for i in range(len(newdf1.iloc[:, 3])):
    # if newdf1.iloc[:, 3].values[i][0] == video_tags[0] and newdf1.iloc[:, 0].values[i] != id:
    if newdf1.iloc[:, 0].values[i] not in id and newdf1.iloc[:, 0].values[i] != '#NAME?':
      similarity_dic = {
          'vid' : newdf1.iloc[:, 0].values[i],
          'similarity' : jaccard_similarity(video_tags, newdf1.iloc[:, 3].values[i])
      }
      similarity_vidoes_score.append(similarity_dic)
  # print(similarity_vidoes_score)
  print(sorted(similarity_vidoes_score, key = lambda i: i['similarity'], reverse=True)[:4])
  # print(video_idx)


  # print(all_same_cat_tags)

recommend(['3Kwpk9J8tJM', 'BgYJmXbIVZo', '6I2yAoxBRtI', 'kJzGH0PVQHQ'])