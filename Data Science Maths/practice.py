import numpy as np
from scipy.stats import norm
import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df=pd.read_csv(url)

sample=df['sepal_length'].sample(30,random_state=42)
mean=sample.mean()
std=sample.std()
n=len(sample)

z_value=norm.ppf(0.975)
margin_of_error=z_value*(std/np.sqrt(n))
ci=(mean - margin_of_error, mean + margin_of_error) #So length of sepal is between 5.6 to 6.3
print(ci)
