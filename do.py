#!/usr/bin/env python
# coding=utf-8
from naiveBayes import NaiveBayes

train_x = [[1,2,3],[2,3,4],[2,1,3]]
train_y = [0,0,1]
nb = NaiveBayes()
nb.fit(train_x,train_y)


