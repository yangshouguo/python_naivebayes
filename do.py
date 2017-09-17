#!/usr/bin/env python
# coding=utf-8
from naiveBayes import NaiveBayes

# S = 'S'
# M = 'M'
# L = 'L'
#
# train_x = [[1,S],[1,M],[1,M],[1,S],[1,S],[2,S],[2,M],[2,M],[2,L],[2,L],[3,L],[3,M],[3,M],[3,L],[3,L]]
# train_y = [-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1]
#
# print train_x
# print train_y
#
# nb = NaiveBayes()
# nb.fit(train_x,train_y)
# result = nb.predict([[2,S]])
# print result


from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import numpy as np
nb = NaiveBayes()
iris =datasets.load_iris()
X_train,X_test,y_train,y_test = train_test_split(iris.data, iris.target, test_size = 0.2, random_state=2333)

nb.fit(X_train.tolist(),y_train.tolist())
y_pred = nb.predict(X_test.tolist())

print y_pred,len(y_pred)
print y_test,y_test.size
print np.mean(np.sqrt(np.square(np.array(y_pred) - y_test)))
#print ("Acc : %f")% np.sqrt(((np.array(y_pred,dtype = 'float64') - y_test)**2).sum()/(y_test.size-1))
