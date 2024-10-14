import pandas as pd
from sklearn import datasets

wine_data = pd.DataFrame(datasets.load_wine().data)
wine_data.columns = datasets.load_wine().feature_names
print(wine_data.head(5))

