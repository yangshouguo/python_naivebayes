#!/usr/bin/env python
# coding=utf-8
from naiveBayes import NaiveBayes

S = 'S'
M = 'M'
L = 'L'

train_x = [[1,S],[1,M],[1,M],[1,S],[1,S],[2,S],[2,M],[2,M],[2,L],[2,L],[3,L],[3,M],[3,M],[3,L],[3,L]]
train_y = [-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1]

print train_x
print train_y

nb = NaiveBayes()
nb.fit(train_x,train_y)
result = nb.predict([[2,S]])
print result

