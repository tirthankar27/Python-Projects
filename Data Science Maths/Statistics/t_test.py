from scipy.stats import ttest_ind

group1 = [2.1, 2.5, 2.8, 3.0, 3.2]
group2 = [1.8, 2.0, 2.4, 2.7, 2.9]

#T-test

t_stat, p_value = ttest_ind(group1, group2)
print("T-Statistics: ",t_stat)
print("P value: ",p_value)

alpha=0.05
if p_value<alpha:
    print("Reject the null hypothesis\nSignificant difference")
else:
    print("Failed to reject the null hypothesis\nNo significant difference")
