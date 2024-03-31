import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as s

coffee = pd.read_csv('starbucks.csv')

## create ages variable
ages = coffee.age

## get min and print
min_age = ages.min()

## get max and print
max_age = ages.max()

## print the range
print(min_age - max_age)

## find the mean
mean_age = np.mean(ages)


## center ages
centered_ages = ages - mean_age

## graph it
plt.hist(centered_ages)
plt.show()