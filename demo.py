#! /bin/python3
#  PAI789 (PJW)
#
#  Illustrate some Seaborn graphs using Pecan Street data
#

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#
#  Set the Seaborn stype
#

sns.set(style="white")

#%%
#
#  Read the dataset: hourly electricity use in kW
#

usage = pd.read_csv('use.csv')

#
#  Trim it down to just January and July for seasonal comparisons
#

janjul = usage.query("month == 1 or month == 7")

#%%
#
#  Figure out mean hourly use
#

by_mo_hr = janjul.groupby(['month','hour'])
hourly = by_mo_hr['usage'].mean()

#  Reset the index to move the month and hour back into the 
#  dataframe as columns. Needed because Seaborn only looks at 
#  the column names when looking for variables

hourly = hourly.reset_index()

#
#  Bar graph of use by hour
#

fig, ax1 = plt.subplots(dpi=300)
sns.barplot(data=hourly,x='hour',y='usage',hue='month',ax=ax1)
ax1.set_title("Average Electricity Usage")
ax1.set_xlabel("Hour")
ax1.set_ylabel("kW")
fig.tight_layout()
fig.savefig('f1_usage.png')

#%%
#
#  Now draw a pair of boxen plots on the overall data 
#  without averaging. Much more detail than a typical 
#  box plot.
#

fig, ax1 = plt.subplots(dpi=300)
sns.boxenplot(data=janjul,x="month",y="usage")
fig.tight_layout()
fig.savefig('f2_boxen.png')

#%%
#
#  Violin plots of the same data. Especially useful here because 
#  the distributions are bimodal, which is not clear from box or 
#  boxen plots.
#

fig, ax1 = plt.subplots(dpi=300)
sns.violinplot(data=janjul,x="month",y="usage")
fig.tight_layout()
fig.savefig('f3_violins.png')

#%%
#
#  Look at the distributions over three particular hours: 8am, 2pm 
#  and 8pm. Use split violins for easy contrast between January and 
#  July.
#

eights = janjul.query("hour==8 or hour==12 or hour==20")
fig, ax1 = plt.subplots(dpi=300)
sns.violinplot(data=eights,x="hour",y="usage",hue="month",split=True)
fig.tight_layout()
fig.savefig('f4_split-violins.png')