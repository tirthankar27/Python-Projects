import numpy as np
from scipy.stats import ttest_1samp,ttest_ind,ttest_rel

#One sample T test
data=[12,14,15,16,17]
population_mid=float(np.median(data))
t_stat,p_value=ttest_1samp(data,population_mid)
print("One-Sample T-Test\n",t_stat,p_value)

#Two sample T test
data1=[12,14,15,16,17]
data2=[11,13,14,15,16]
t_stat,p_value=ttest_ind(data1,data2)
print("Two-Sample T-Test\n",t_stat,p_value)

#Paired sample T test
pre_test=[12,14,15,16,17]
post_test=[13,14,16,17,18]
t_stat,p_value=ttest_rel(pre_test,post_test)
print("Paired-Sample T-Test\n",t_stat,p_value)
