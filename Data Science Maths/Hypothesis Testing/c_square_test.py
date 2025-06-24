import numpy as np
from scipy.stats import chi2_contingency

#Contingency Table
data=[[50,30,20],[30,40,30]]

#Chi-Square Test
chi2, p_value, dof, expected=chi2_contingency(data)

print(f"Chi-Square Statistic: {chi2}")
print(f"P-values: {p_value}")
print(f"Expected frequencies:\n {expected}")
