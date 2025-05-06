# Importando as bibliotecas necessárias
import numpy as np
import pandas as pd
from sklearn import datasets

# Carregando o dataset Iris
iris = datasets.load_iris()

# Extraindo os dados e criando um DataFrame
X = iris.data  # Características (features)
y = iris.target  # Classes (target)
feature_names = iris.feature_names
target_names = iris.target_names

# Criando um DataFrame para melhor visualização
df = pd.DataFrame(X, columns=feature_names)
df['species'] = [target_names[i] for i in y]

# Visualizando as primeiras linhas do dataset
print("Primeiras linhas do dataset Iris:")
print(df.head())


# Importando as bibliotecas necessárias
import pandas as pd
import requests
import io

# URL do dataset Iris no UCI Repository
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# Baixando e carregando o dataset
iris_data = requests.get(url).content
df = pd.read_csv(io.StringIO(iris_data.decode('utf-8')), names=names)

# Visualizando as primeiras linhas do dataset
print("Primeiras linhas do dataset Iris:")
print(df.head())

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, roc_curve, auc, mean_absolute_error, mean_squared_error, r2_score

# Substitua 'caminho_do_arquivo' pelo local onde você salvou o arquivo
df = pd.read_csv('iris.csv')

X_train, X_test, Y_train, Y_test = train_test_split(iris.data, iris.target, test_size=0.3)

knn = KNeighborsClassifier()

knn.fit(X_train, Y_train)

y_pred = knn.predict(X_test)


acuracia = knn.score(X_test, Y_test)
mae = mean_absolute_error(Y_test, y_pred)
precision = precision_score(Y_test, y_pred ,average='weighted')
recall  = recall_score(Y_test, y_pred, average='weighted')
f1 = f1_score(Y_test, y_pred, average='weighted')

print("ACURACIA")
print(acuracia)
print("MAE")
print(mae)
print("PRE")
print(precision)
print("RECALL")
print(recall)
print("F1")
print(f1)







# Visualizando as primeiras linhas do dataset
print(df.head())