"""
demo.py
Spring 2022 PJW

Illustrate some Seaborn graphs using Pecan Street data
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#
#  Set the default Matplotlib resolution and Seaborn style
#

plt.rcParams['figure.dpi'] = 300
sns.set_theme(style="white")

#%%
#
#  Read the dataset: hourly electricity use in kW
#

usage = pd.read_csv('use.csv')

#%%
#
#  Pivot the data to have one column for each hour, and then compute each
#  hour's usage as a percent of the day's
#

by_day_use = usage.pivot(index=['month','day'],columns='hour',values='usage')

by_day_tot = by_day_use.sum(axis='columns')
by_day_pct = 100*by_day_use.div(by_day_tot,axis='index')

#
#  Now compute the mean percentages by month
#

means = by_day_pct.groupby('month').mean()

#
#  Convert to long form for seaborn. Reset the index to move the month into the
#  columns of the data frame so it can be used as the ID variable.
#

long_form = means.reset_index().melt(id_vars='month')

#
#  Draw a line plot of mean daily percentage by hour and month
#

fig,ax = plt.subplots()
sns.lineplot(data=long_form,x='hour',y='value',hue='month',palette='viridis',ax=ax)
fig.suptitle('Mean Use by Hour and Month')
ax.set_xlabel('Hour')
ax.set_ylabel('Percent of Daily Electricity Use')
fig.tight_layout()

#%%
#
#  Now trim it down to just January and July for seasonal comparisons
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
#  Bar graph of use by hour.
#
#  This treats hue as a categorical value. As of seaborn 0.13, the
#  default palette for categorical values is unpleasant so change it to
#  seaborn's general default palette, "deep".
#

fig, ax1 = plt.subplots()
sns.barplot(data=hourly,x='hour',y='usage',
            hue='month',palette='deep',ax=ax1)
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

fig, ax1 = plt.subplots()
sns.boxenplot(data=janjul,x="month",y="usage")
fig.tight_layout()
fig.savefig('f2_boxen.png')

#%%
#
#  Violin plots of the same data. Especially useful here because
#  the distributions are bimodal, which is not clear from box or
#  boxen plots.
#

fig, ax1 = plt.subplots()
sns.violinplot(data=janjul,x="month",y="usage")
fig.tight_layout()
fig.savefig('f3_violins.png')

#%%
#
#  Look at the distributions over three particular hours: 8am, 2pm
#  and 8pm. Use split violins for easy contrast between January and
#  July.
#
#  The hue variable will be treated as categorical, so specify an
#  improved palette.


eights = janjul.query("hour==8 or hour==12 or hour==20")
fig, ax1 = plt.subplots()
sns.violinplot(data=eights,x="hour",y="usage",
               hue="month",palette='deep',split=True)
fig.tight_layout()
fig.savefig('f4_split-violins.png')

#%%
#
#  Draw a hex plot showing the joint distribution of hourly loads in
#  January and July.
#

bymo = janjul.set_index(['month','day','hour'])
bymo = bymo.unstack('month')
print(bymo)

bymo = bymo['usage']

jg = sns.jointplot(data=bymo,x=1,y=7,kind='hex')
jg.fig.suptitle('Distribution of Hourly Load')
jg.fig.tight_layout()
jg.set_axis_labels('January','July')

jg.savefig('f5_hex.png')
