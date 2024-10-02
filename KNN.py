import numpy as np
import pandas as pd
import matplotib.pyplot as plt


from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from scipy.stats import mode


dataset = pd.read_csv()
dataset.head()




dataset = dataset.drop('Gender',axis=1)
dataset.head()




X = dataset.drop('Purchase Iphone',axis=1)
Y = dataset.head['Purchase Iphone']

print(X)
print(Y)

sns.displot(dataset, X = 'Salary', hue = 'Purchase Iphone')


def euclidean_distance(pt1,pt2):
    distance = np.sqrt(np.sum(pt1-pt2)**2)
    return distance

a = np.array([3,4])
b = np.array([5,9])

print(euclidean_distance(a,b))

def KNN(X_train, X_test, Y_train, Y_test,k_val):
    y_hat = []
    for test_pt in X_test.to_numpy():
        distances = []
        for i in range(len(X_train)):
            distances.append(euclidean_distance(np.array(X_train.iloc[i])), tes_pt)
            
        distance_data = pd.DataFramr(data = distance,columns=['distance'], index= Y_train.index)
        
        K_neighbors_list = distance_data.sort_values(by=['distance'], axis=0)[:k_val]
        
        labels = Y_train.loc[K_neighbors_list.index]
        
        voting = mode(labels).mode[0]
        
        y_hat.append(voting)
    return y_hat

x_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = .3, random_state=42)
y_hat_test = KNN(X_train, X_test, Y_train, Y_test,k_val=5)
        
accuracy_vals = []
for i in range(1,15):
    y_hat_test = KNN(X_train, X_test, Y_train, Y_test,k_val=i)
    accuracy_vals.append(accuracy_score(Y_test,y_hat_test))
plt.plot(range(1,15), accuracy_vals, color='blue', marker='x', linestyle='dashed')



y_hat_test = KNN(X_train, X_test, Y_train, Y_test,k_val=5)
print(accuracy_score(Y_test, y_hat_test))

for i in range(len(y_hat_test)):
    if(y_hat_test[i]==0):
        plt.scatter(X_test.iloc[i]['Age'], X_test.iloc[i]['Salary'], color ='blue')
    if(y_hat_test[i]==1):
        plt.scatter(X_test.iloc[i]['Age'], X_test.iloc[i]['Salary'], color ='orange')
plt.style.use('ggplot')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.titl('KNN Results')

    
