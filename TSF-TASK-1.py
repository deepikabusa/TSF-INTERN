import pandas as pd
import numpy as np  
from matplotlib import pyplot
# %matplotlib inline


url = "http://bit.ly/w-data"
s_data = pd.read_csv(url)
print("Data imported successfully")

s_data.head(5)


s_data.plot(x='Hours', y='Scores', style='*')  
pyplot.title('Hours of learning impact on Percentage')  
pyplot.xlabel('Hours Studied')  
pyplot.ylabel('Percentage Score')  
pyplot.show()
