#来自Bitly的USA.gov

import numpy as np
path = 'H:/ML/pydata-book-2nd-edition/datasets/bitly_usagov/example.txt'
print(open(path).readlines())

import json
records = [json.loads(line) for line in open(path)]
print(records[0])


#用纯Python代码对时区进行计数
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print(time_zones[:10])

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

from collections import defaultdict
def get_counts2(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts

counts = get_counts(time_zones)
print(counts['America/New_York'])
print(len(time_zones))

def top_counts(count_dict,n=10):
    value_key_pairs = [(count,tz) for tz,count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
print(top_counts(counts))

from collections import Counter
counts = Counter(time_zones)
print(counts.most_common(10))

#用pandas对时区进行计数
import pandas as pd
frame = pd.DataFrame(records)
print(frame.info())
print(frame['tz'][:10])

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print(tz_counts[:10])

import seaborn as sns
subset = tz_counts[:10]
sns.barplot(y=subset.index,x=subset.values)

results = pd.Series([x.split()[0] for x in frame.a.dropna()])
print(results[:5])
print(results.value_counts()[:8])

cframe = frame[frame.a.notnull()]
cframe['os'] = np.where(cframe['a'].str.contains('Windows'),
                        'Windows','Not Windows')
print(cframe['os'][:5])
by_tz_os = cframe.groupby(['tz','os'])
agg_counts = by_tz_os.size().unstack().fillna(0)
print(agg_counts[:10])
indexer = agg_counts.sum(1).argsort()
print(indexer[:10])

count_subset = agg_counts.take(indexer[-10:])
print(count_subset)

print(agg_counts.sum(1).nlargest(10))