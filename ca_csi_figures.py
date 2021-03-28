#! /bin/python3
#  Spring 2020 (PJW)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#
#  Read the dataset
#

pv = pd.read_pickle('ca_csi_2020.pkl')

#%%

#
#  Describe it briefly
#

print('\nDataframe information:\n')
print( pv.info() )

catvars = ['app_status','sector','state','third_party','inst_status','type','year']
    
for v in catvars:
    print('\n'+v+':\n')
    print( pv[v].value_counts() )

#%%

#
#  Quick plots of key attributes
#

sns.set(style='white')

for v in catvars:
    sns.catplot(y=v,kind='count',data=pv)

#%%

#
#  Focus on a subset of the data
#

res = pv.query("sector == 'Residential' & app_status == 'Completed'")
res = res.query("inst_status == 'Installed'")

print('\nOriginal records:',len(pv))
print('Trimmed records:',len(res))

#%%

# 
#  Check interesting variables in trimmed dataset; save the figures 
#  while we're at it.
#

for v in ['third_party','year']:
    fg = sns.catplot(y=v,kind='count',data=res)
    fg.savefig('res_'+v+'.png')

#%%

#
#  Draw some histograms. Use plt.figure() to make sure they use 
#  different axes. Needed because distplot() returns an axis 
#  object, which is part of a figure and allows for overlaying
#  plots.
#

plt.figure()
ax = sns.distplot(res['nameplate'])

plt.figure()
ax = sns.distplot(res['total_cost'])

#%%

#
#  Trim the data set down to more typical residential 
#  installations.
#

trim = res.query("nameplate < 20 and total_cost < 160000")

print('\nTrimmed records:',len(trim))

#%%

#
#  Draw the new histograms and save them along the way.
#

plt.figure()
ax = sns.distplot(trim['nameplate'])
plt.savefig('res_nameplate.png')

plt.figure()
ax = sns.distplot(trim['total_cost'])
plt.savefig('res_total_cost.png')

#%%

#
#  Other ways to look at the distribution
#
              
plt.figure()
ax = sns.boxenplot(trim['nameplate'],orient='h')
plt.savefig('res_boxen_all.png')

plt.figure()
ax = sns.violinplot(trim['nameplate'],orient='h')
plt.savefig('res_violin.png')

#%%

#
#  More detail: nameplate by year
#

plt.figure()
ax = sns.boxenplot(y='year',x='nameplate',orient='h',data=trim)
plt.savefig('res_boxen_year.png')

#%%

#
#  Plot the joint distribution using a hex plot
#

jg = sns.jointplot('nameplate', 'total_cost', data=trim,kind='hex')
jg.savefig('res_hexbin.png')

#%%

#
#  Contour plot: nice but slow on large data sets
#

#jg = sns.jointplot('nameplate', 'total_cost', data=trim,kind='kde')
#jg.savefig('res_contour.png')

