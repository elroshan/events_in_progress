import json
from overlap_determiner import max_overlap

f = open('../data.json')
data = json.load(f)
max_parallel_views = max_overlap(data['VideoPlay'])

print(f"Maximum number of plays for the given dataset is : {max_parallel_views}")

f.close()


