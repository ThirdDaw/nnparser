from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

iris = datasets.load_iris()

print(iris.feature_names)

print(iris.target_names)

print(iris.data)

print(iris.target)

X = iris.data
Y = iris.target

print(X.shape)
print(Y.shape)

clf = RandomForestClassifier()
clf.fit(X, Y)


print(clf.feature_importances_)

print(clf.predict([[5.1, 3.5, 1.4, 0.2]]))

print(clf.predict(X[[0]]))

print(clf.predict_proba(X[[0]]))

clf.fit(iris.data, iris.target_names[iris.target])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

print(X_train.shape, Y_train.shape)

print(X_test.shape, Y_test.shape)

clf.fit(X_train, Y_train)
