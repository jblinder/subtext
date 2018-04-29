import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dateutil.parser
import seaborn as sns
from IPython.display import Image

# enables inline plots, without it plots don't show up in the notebook
%matplotlib inline
%pylab inline

''' Settings '''
sns.set_style("white")
pd.set_option('display.max_columns', 25)
pd.set_option('display.max_rows', 25)
pd.set_option('display.precision', 3)

''' Load and concatinate CSV files into single dataframe'''
csv_names = ['/Users/justinblinder/Desktop/subtitles-parser-master/vertigo.csv','/Users/justinblinder/Desktop/subtitles-parser-master/12monkeys.csv','/Users/justinblinder/Desktop/subtitles-parser-master/BlackPanther.csv','/Users/justinblinder/Desktop/subtitles-parser-master/AlmostFamous.csv','/Users/justinblinder/Desktop/subtitles-parser-master/Goodfellas.csv']
files=[]
for path in csv_names:
    files.append(
        pd.read_csv(path)
    )
df = pd.concat(files)


df['duration'] = df['endTime'] - df['startTime']


df['delta'] = df.groupby('movie')['endTime'].transform(pd.Series.diff)

vertigo = df[df['movie'] == 'Black Panther']
#vertigo.sort_values('delta',ascending=False)
#plt.hist([vertigo['startTime'],vertigo['delta']],bins=100)
v = vertigo[vertigo['duration'] > 100]
plt.hist([v['startTime'],v['duration']],bins=100)

df