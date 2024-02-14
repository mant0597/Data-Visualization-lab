import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'man.txt'
data_list=[]

with open(file_path,'r') as file:
    for line in file:
        data_point=float(line.strip())
        data_list.append(data_point)
print("Data List:",data_list)
sns.histplot(data_list,kde=True)
plt.show()