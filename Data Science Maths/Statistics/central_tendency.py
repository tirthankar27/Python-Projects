import numpy as np
from statistics import mode
my_list=[10,20,30,40,50]
print("Mean: ",np.mean(my_list))
print("Median: ",np.median(my_list))
print("Mode: ",mode(my_list))
print("Variance: ",np.var(my_list))
print("Standard deviation: ",np.sqrt(np.var(my_list)))

x=np.mean(my_list)
z_score=1.96
ci = x + z_score * (np.sqrt(np.var(my_list)) / len(my_list)), x - z_score * (np.sqrt(np.var(my_list)) / len(my_list))
print("95% Confidence Interval: ",ci)