import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
import statistics
import numpy as np
sns.set(color_codes=True)
sugar = pd.read_csv('CEN414DATA.csv')
sugar.info()
sugar 
 
plt.gca().margins(x=0)
plt.gcf().canvas.draw()
tl = plt.gca().get_xticklabels()
maxsize = max([t.get_window_extent().width for t in tl])
m = 0.2 # inch margin
s = maxsize/plt.gcf().dpi*60+2*m
margin = m/plt.gcf().get_size_inches()[0]

plt.gcf().subplots_adjust(left=margin, right=1.-margin)
plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])
plt.legend(loc='upper right')
sns.barplot(sugar['Code'],sugar['Sugar cane-Yield-hg/ha'],  sugar['Year'])
plt.savefig("C:\CLOUDDATA2.png")

sugar2 = sugar.set_index('Code')

for i in range(5):
    l = 2009+i*2
    h = l + 2
    fig, axes  = plt.subplots(1,2, figsize=(20,10))

    for idx, year in enumerate(range(l,h)):
        sugar2[sugar2['Year'] == year]['Sugar cane-Yield-hg/ha'].plot.barh(ax=axes[idx])

        axes[idx].set_title(year)
    plt.savefig(f"C:\CLOUDDATA3_{i}.png")      

sns.boxplot(sugar['Code'],sugar['Sugar cane-Yield-hg/ha'],  sugar['Year'])
plt.gca().margins(x=0)
plt.gcf().canvas.draw()
tl = plt.gca().get_xticklabels()
maxsize = max([t.get_window_extent().width for t in tl])
m = 0.2 # inch margin
s = maxsize/plt.gcf().dpi*46+2*m
margin = m/plt.gcf().get_size_inches()[0]

plt.gcf().subplots_adjust(left=margin, right=1.-margin)
plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])

plt.show()

plt.gca().margins(x=0)
plt.gcf().canvas.draw()
tl = plt.gca().get_xticklabels()
maxsize = max([t.get_window_extent().width for t in tl])
m = 0.2 # inch margin
s = maxsize/plt.gcf().dpi*46+2*m
margin = m/plt.gcf().get_size_inches()[0]

plt.gcf().subplots_adjust(left=margin, right=1.-margin)
plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])
sns.pointplot(sugar['Code'],sugar['Sugar cane-Yield-hg/ha'],  sugar['Year']) 
plt.savefig("C:\CLOUDDATA5.png") 

plt.gca().margins(x=0)
plt.gcf().canvas.draw()
tl = plt.gca().get_xticklabels()
maxsize = max([t.get_window_extent().width for t in tl])
m = 0.2 # inch margin
s = maxsize/plt.gcf().dpi*46+2*m
margin = m/plt.gcf().get_size_inches()[0]

plt.gcf().subplots_adjust(left=margin, right=1.-margin)
plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])
sns.stripplot(sugar['Code'],sugar['Sugar cane-Yield-hg/ha'],  sugar['Year']) 
plt.savefig("C:\CLOUDDATA6.png")

plt.figure(figsize=(10,10))

def interquartile_range(sample):
    q3, q1 = np.percentile(sample, [75 ,25])
    return q3 - q1

def quartile_range(sample):
    q3, q1 = np.percentile(sample, [75 ,25])
    return (q3 - q1)/2

def _range(sample):
    return sample.max() - sample.min()

def create_plot(fn, label):
    ls = []
    for year in range(2009,2018):
            ls.append(fn(sugar[sugar['Year'] == year]['Sugar cane-Yield-hg/ha']))
              
    plt.plot(range(2009,2018), ls, label=label)
    plt.title('Measures of Dispersion of African Countries against Year.')
    plt.ylabel('Sugar cane-Yield-hg/ha')
    plt.xlabel('Year')
    
create_plot(statistics.mean, 'Mean')
#create_plot(statistics.variance, 'Variance')
#create_plot(statistics.stdev, 'Standard Deviation')
create_plot(interquartile_range, 'Interquartile Range')
create_plot(quartile_range, 'Quartile Range')
create_plot(_range, 'Range')

plt.legend(loc='best')
plt.savefig("C:\CLOUDDATA7.png")

create_plot(statistics.variance, 'Variance')
create_plot(_range, 'Range')
plt.legend(loc='best')
plt.savefig("C:\CLOUDDATA8.png")

create_plot(statistics.stdev, 'Standard Deviation')
plt.legend(loc='best')
plt.savefig("C:\CLOUDDATA9.png")

 