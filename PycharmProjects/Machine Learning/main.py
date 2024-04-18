# # first ml model by codewithharry
# # diabetes model

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error

diabetes=datasets.load_diabetes()
print(diabetes.keys())
# (['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename'])
# print(diabetes.DESCR)
diabetes_X=diabetes.data[:,np.newaxis,2]
# print(diabetes_X)
diabetes_X_train=diabetes_X[:-30]
diabetes_X_test=diabetes_X[-30:]
diabetes_y_train=diabetes.target[:-30]
diabetes_y_test=diabetes.target[-30:]
model=linear_model.LinearRegression()
model.fit(diabetes_X_train,diabetes_y_train)
diabetes_y_predict=model.predict(diabetes_X_test)
print("Mean square error is:",mean_squared_error(diabetes_y_test,diabetes_y_predict))
print("Weights:",model.coef_)
print("Intercepts:",model.intercept_)
plt.scatter(diabetes_X_test,diabetes_y_test)
plt.plot(diabetes_X_test,diabetes_y_predict)
plt.show()





# from matplotlib import pyplot as plt
#
# x=[1,4,9]
# y=[4,5,6]
# x2=[2,4,6,7]
# y2=[5,2,7,9]
#
# plt.hist(x,y)
# plt.plot(x,y)
# plt.scatter(x,y)
# plt.plot(x2,y2)
# plt.scatter(x2,y2)
# plt.title("My graph")
# plt.xlabel("X axis")
# plt.ylabel("Y axis")
# plt.legend()
# plt.show()


