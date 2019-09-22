import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv', sep=',', header=None, names=('sepal_length','sepal_width','petal_length','petal_width','species'))
iris_species_arr = df['species'].unique()

# sepal_length
for index, item in enumerate(iris_species_arr):
    data = df.query('species=="'+item+'"')['sepal_length']
    sns.distplot(data,kde=False,rug=False,label=item)

plt.legend()
plt.show()

# sepal_width
for index, item in enumerate(iris_species_arr):
    data = df.query('species=="'+item+'"')['sepal_width']
    sns.distplot(data,kde=False,rug=False,label=item)

plt.legend()
plt.show()

# petal_length
for index, item in enumerate(iris_species_arr):
    data = df.query('species=="'+item+'"')['petal_length']
    sns.distplot(data,kde=False,rug=False,label=item)

plt.legend()
plt.show()

# petal_width
for index, item in enumerate(iris_species_arr):
    data = df.query('species=="'+item+'"')['petal_width']
    sns.distplot(data,kde=False,rug=False,label=item)

plt.legend()
plt.show()
