

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
file_path = 'man.csv'
df = pd.read_csv(file_path)
print("Columns in the DataFrame:")
print(df.columns)
sns.set(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.scatterplot(x="min_price", y="max_price", data=df, palette="Set2")
plt.title('Scatter Plot of Min Price vs Max Price')
plt.xlabel('Min Price')
plt.ylabel('Max Price')
plt.show()