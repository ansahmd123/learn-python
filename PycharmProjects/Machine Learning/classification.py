# model 2:iris model classifier with Kneighbour classifier

# import modules
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# import datasets
file=datasets.load_iris()

# feeding data
features=file.data
labels=file.target

# create classifier
cls=KNeighborsClassifier()

# train classifier
cls.fit(features,labels)

# prediction
result=cls.predict([[1,2,3,4]])
print(result)







