import numpy as np

outcomes=np.arange(1,7)
probabilities=np.array([1/6]*6)

#Expectation
expectation=np.sum(outcomes * probabilities)

print(f"Expectation: {expectation}")

#variance
variance= (np.sum(outcomes**2 * probabilities)) - expectation**2 # np.sum((outcomes - expectation)**2 * probabilities)
print(f"Variance: {variance}")
print(f"Standard deviation: {np.sqrt(variance)}")