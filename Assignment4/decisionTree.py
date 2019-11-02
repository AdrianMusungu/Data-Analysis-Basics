import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

#importing the Iris csv
df = pd.read_csv('iris.csv', names = ['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm','Species'])
#print df

#Creating the train and test sets
X = df.drop('Species', axis =1)
y = df['Species']
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=1)

#Creating the decision tree
dTree = DecisionTreeClassifier(criterion='entropy')
dTree.fit(X_train,y_train)

y_pred = dTree.predict(X_test)

#Getting the accuracy score
score = accuracy_score(y_test,y_pred)
print score
