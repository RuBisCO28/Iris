import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv', sep=',', header=None, names=('sepal_length','sepal_width','petal_length','petal_width','species'))
g = sns.pairplot(df,hue = "species",diag_kind="kde")
plt.show()
