#!/usr/bin/env python
# coding=utf-8


class NaiveBayes(object):
    def __init__(self):
        self._train_x = []
        self._train_y = []
        self._tags = set() #所有可能的分类
        self._prioriprob = {} #记录每类的先验概率值
        self._trainsetSize = 0
        self._dim = 0 # 数据维度
        self._conditionprob = [] # 所有维度的条件概率 某一属性的条件概率表示P(xi|ck) {xi:{ck:p}}\
        self._conditionprob_var={}
        self._lambda = 1 # 采用贝叶斯估计参数
        self._S = [] #记录每种特征的种类数
        pass

    #计算先验概率
    def _compute_PrioriProbability(self):
        self._tags = set(self._train_y)
        for item in self._tags:
            self._prioriprob.update({item: (self._train_y.count(item)*1.0+self._lambda)/(self._trainsetSize+self._lambda*len(self._tags))})

    # 计算条件概率P(xi|ck) = N(xi,ck) / N(ck)
    def _compute_conditionProbability_varDim(self):
        pass

        #self._S 记录某个单词在一句中出现不同次数的种类数
        self._S={}



        for i in range(self._trainsetSize):
            if not self._conditionprob_var.has_key(self._train_y[i]):
                self._conditionprob_var.update({self._train_y[i]:{}})
            for item in self._train_x[i]:

                if not self._S.has_key(item):
                    self._S.update({item:set()})

                self._S[item].add(self._train_x[i][item])


                if not self._conditionprob_var[self._train_y[i]].has_key(item):
                    self._conditionprob_var[self._train_y[i]].update({item:{}})
                if not self._conditionprob_var[self._train_y[i]][item].has_key(self._train_x[i][item]):
                    self._conditionprob_var[self._train_y[i]][item].update({self._train_x[i][item]:1})
                else:
                    self._conditionprob_var[self._train_y[i]][item][self._train_x[i][item]]+= 1

        tmp = {}
        for item in self._conditionprob_var:
            if not tmp.has_key(item):
                tmp.update({item:{}})
            for item2 in self._conditionprob_var[item]:
                if not tmp[item].has_key(item2):
                    tmp[item].update({item2:{}})
                for item3 in self._conditionprob_var[item][item2]:
                    if not tmp[item][item2].has_key(item3):
                        tmp[item][item2].update({item3:1})
                    tmp[item][item2][item3] = self._conditionprob_var[item][item2][item3]*1.0/self._train_y.count(item)

        self._conditionprob_var = tmp

        
    def fit(self, train_x, train_y):
        self._train_x = train_x
        self._train_y = train_y
        if (len(train_x) == len(train_y)):
            self._trainsetSize = len(train_x) # trainset size
            self._dim = len(train_x[0])
        else:
            #print 'dataset error'
            return
        self._compute_PrioriProbability()
        self._compute_conditionProbability_varDim()
        pass
        
    # y = argmax (P(ck) II(P(xi,ck)))

    def predict_varfeature(self, test_x):
        result = []
        # print self._conditionprob
        # print 'prioriprob'
        # print self._prioriprob
        for i in range(len(test_x)):
            max_prob = 0
            t_ck = ''
            prob = 1
            for ck in self._tags:
                for xi in test_x[i]:
                    # print i,xi , test_x[i][xi],ck

                    if (self._conditionprob_var[ck].has_key(xi) and self._conditionprob_var[ck][xi].has_key(test_x[i][xi])):
                        prob *= self._conditionprob_var[ck][xi][test_x[i][xi]]
                    else:
                        prob *= 1.0*self._lambda/(self._train_y.count(ck)+len(self._S[xi]))#!!!!!!!!!!!!!!!!!!!!! not to modify
                prob *= self._prioriprob[ck]
                # print  ('sample:',test_x[i],' be',ck,'has ',prob,' probability')
                if (prob >= max_prob):
                    max_prob = prob
                    t_ck = ck
                prob = 1
            if (t_ck != ''):
                result.append(t_ck)

        return result
