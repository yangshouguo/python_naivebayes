#!/usr/bin/env python
# coding=utf-8


class NaiveBayes(object):
    def __init__(self):
        self._train_x = []
        self._train_y = []
        self._tags = set()
        self._prioriprob = {} #记录每类的先验概率值
        self._trainsetSize = 0
        self._dim = 0 # 数据维度
        self._conditionprob = [] # 所有维度的条件概率
        pass

    #计算先验概率
    def _compute_PrioriProbability(self):
        self._tags = set(self._train_y)
        for item in self._tags:
            self._prioriprob.update({item: self._train_y.count(item)*1.0/self._trainsetSize})
    
    #计算条件概率P(xi|ck) = I(xi,ck) / I(ck)
    def _compute_ConditionProbability(self):
        
        for i in range(self._dim):
            self._conditionprob.append({})

        for i in range(self._dim):
            tmp = {}
            for j in range(self._trainsetSize):
                if (tmp.has_key(self._train_x[j][i])):
                    if (tmp[self._train_x[j][i]].has_key(self._train_y[j])):
                        tmp[self._train_x[j][i]][self._train_y[j]]+=1
                    else:
                        tmp[self._train_x[j][i]].update({self._train_y[j]:1})
                else:
                    tmp.update({self._train_x[j][i]:{self._train_y[j]:1}})
            
            for item in tmp:
                for item2 in tmp[item]:
                    #print 'i:',i,item,item2,tmp[item][item2]
                    if (self._conditionprob[i].has_key(item)):
                        self._conditionprob[i][item].update({item2:tmp[item][item2]*1.0/self._train_y.count(item2)})
                    else:
                        self._conditionprob[i].update({item:{item2:tmp[item][item2]*1.0/self._train_y.count(item2)}})

        #print self._conditionprob

        pass 
        
    def fit(self, train_x, train_y):
        self._train_x = train_x
        self._train_y = train_y
        if (len(train_x) == len(train_y)):
            self._trainsetSize = len(train_x)
            self._dim = len(train_x[0])
        else:
            #print 'dataset error'
            return
        self._compute_PrioriProbability()
        self._compute_ConditionProbability() 
        pass
        

    def predict(self, test_x):
        result = []
        for i in range(len(test_x)):
            pass
        pass
