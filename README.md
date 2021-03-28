# Example: Data Visualization Using Seaborn, Part I

### Summary

Script `ca_csi_figures.py` demonstrates several ways to visualize 
data using Seaborn and Pandas. The data used comes from the 
California Solar Initiative databank available at the 
URL below. However, a number of the original columns that are 
not used in the examples been omitted.

### Input Data

The input data is file `ca_csi_2020.pkl` in the course Google Drive
folder `x01-seaborn-1`. The original source of the data was
[https://www.californiadgstats.ca.gov/downloads/](
https://www.californiadgstats.ca.gov/downloads/)

### Some of the Examples

#### catplot() with kind='count'

![res_third_party.png](res_third_party.png)

![res_year.png](res_year.png)

#### distplot()

![res_nameplate.png](res_nameplate.png)

![res_total_cost.png](res_total_cost.png)

#### boxenplot() 

![res_boxen_all.png](res_boxen_all.png)

![res_boxen_year.png](res_boxen_year.png)

#### violinplot()

![res_violin.png](res_violin.png)

#### jointplot() with kind='hex'

![res_hexbin.png](res_hexbin.png)

#### jointplot() with kind='kde'

![res_contour.png](res_contour.png)
