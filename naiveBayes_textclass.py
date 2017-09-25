#!/usr/bin/env python
# coding=utf-8


# 基于朴素贝叶斯的文本分类器，采用多项式模型处理单词出现重复性问题
import math
import collections

class NaiveBayes(object):
    def __init__(self):
        self._train_x = []
        self._train_y = []
        self._tags = set() #类别集合

        self._prioriprob = collections.defaultdict(float) #记录每类的先验概率值 p(ck) = N(ck下单词总数)／N(文档单词总数)

        self._trainsetSize = 0

        # 类条件概率 某一属性的条件概率表示P(xi|ck)
        self._conditionprob_var={}
        self._lambda = 1 # 采用贝叶斯估计参数

        self._S = [] #记录某一类下单词总数
        self._worddic = set() #总单词表
        self._word_num =0 #总的单词数量
        self._classkind = collections.defaultdict(int)

        pass

    #计算先验概率
    def _compute_PrioriProbability(self):
        # print '总单词量',self._word_num
        # all = 0
        for item in self._S:
            # print item,self._S[item]
            self._prioriprob[item] = self._S[item]*1.0 / self._word_num
            # print item,self._prioriprob[item]
            # all+=self._prioriprob[item]

        # print '总',all



    # 计算条件概率P(xi|ck) = N(xi,ck) / N(ck)   多项式模型
    def _compute_conditionProbability_varDimB(self):
        pass

        #self._S 记录某个单词在一句中出现不同次数
        self._S= collections.defaultdict(int)
        self._conditionprob_var = collections.defaultdict(dict)

        for i in range(self._trainsetSize):

            for item in self._train_x[i]:
                self._S[self._train_y[i]]+=self._train_x[i][item]
                self._word_num += self._train_x[i][item]
                self._worddic.add(item)
                if not self._conditionprob_var[self._train_y[i]].has_key(item):
                    self._conditionprob_var[self._train_y[i]].update({item:0})
                self._conditionprob_var[self._train_y[i]][item]+= self._train_x[i][item]


        tmp = collections.defaultdict(dict)

        for item in self._conditionprob_var:
            for item2 in self._conditionprob_var[item]:
                if not tmp[item].has_key(item2):
                    tmp[item].update({item2:1})
                tmp[item][item2] = (self._conditionprob_var[item][item2]+1)*1.0 / (self._S[item]+len(self._worddic)) #平滑

        self._conditionprob_var = tmp




        
    def fit(self, train_x, train_y):
        self._train_x = train_x
        self._train_y = train_y
        if (len(train_x) == len(train_y)):
            self._trainsetSize = len(train_x) # trainset size
            self._tags = set(train_y)
        else:
            #print 'dataset error'
            return

        self._compute_conditionProbability_varDimB()
        self._compute_PrioriProbability()
        pass







    # y = argmax (P(ck) II(P(xi,ck)))

    def predict_varfeature(self, test_x):
        result = []



        for i in range(len(test_x)):


            max_prob = -100000
            t_ck = ''
            prob = 0
            for ck in self._tags:

                for xi in test_x[i]:
                    # print i,xi , test_x[i][xi],ck

                    if (self._conditionprob_var[ck].has_key(xi) ):
                        prob += math.log(self._conditionprob_var[ck][xi])
                    else:
                        prob += math.log(1.0*self._lambda/(self._S[ck]+len(self._worddic)))#!!!!!!!!!!!!!!!!!!!!! not to modify
                prob += self._prioriprob[ck]
                # print  ('sample:',test_x[i],' be',ck,'has ',prob,' probability')
                if (prob >= max_prob):
                    max_prob = prob
                    t_ck = ck
                prob = 0
            if (t_ck != ''):
                result.append(t_ck)

        return result
