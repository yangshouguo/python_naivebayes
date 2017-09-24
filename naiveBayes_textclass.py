#!/usr/bin/env python
# coding=utf-8


# 基于朴素贝叶斯的文本分类器，采用多项式模型处理单词出现重复性问题
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

        pass

    #计算先验概率
    def _compute_PrioriProbability(self):

        for item in self._S:
            self._prioriprob[item] = self._S[item]*1.0 / self._word_num



    # # 计算条件概率P(xi|ck) = N(xi,ck) / N(ck)   ???正确率34%
    # def _compute_conditionProbability_varDim(self):
    #     pass
    #
    #     #self._S 记录某个单词在一句中出现不同次数的种类数
    #     self._S={}
    #
    #
    #
    #
    #     for i in range(self._trainsetSize):
    #         if not self._conditionprob_var.has_key(self._train_y[i]):
    #             self._conditionprob_var.update({self._train_y[i]:{}})
    #         for item in self._train_x[i]:
    #
    #             if not self._S.has_key(item):
    #                 self._S.update({item:set()})
    #
    #             self._S[item].add(self._train_x[i][item])
    #
    #
    #             if not self._conditionprob_var[self._train_y[i]].has_key(item):
    #                 self._conditionprob_var[self._train_y[i]].update({item:{}})
    #             if not self._conditionprob_var[self._train_y[i]][item].has_key(self._train_x[i][item]):
    #                 self._conditionprob_var[self._train_y[i]][item].update({self._train_x[i][item]:1})
    #             else:
    #                 self._conditionprob_var[self._train_y[i]][item][self._train_x[i][item]]+= 1
    #
    #     tmp = {}
    #     for item in self._conditionprob_var:
    #         if not tmp.has_key(item):
    #             tmp.update({item:{}})
    #         for item2 in self._conditionprob_var[item]:
    #             if not tmp[item].has_key(item2):
    #                 tmp[item].update({item2:{}})
    #             for item3 in self._conditionprob_var[item][item2]:
    #                 if not tmp[item][item2].has_key(item3):
    #                     tmp[item][item2].update({item3:1})
    #                 tmp[item][item2][item3] = self._conditionprob_var[item][item2][item3]*1.0/self._train_y.count(item)
    #
    #     self._conditionprob_var = tmp


    # 计算条件概率P(xi|ck) = N(xi,ck) / N(ck)   多项式模型
    def _compute_conditionProbability_varDimB(self):
        pass

        #self._S 记录某个单词在一句中出现不同次数
        self._S= collections.defaultdict(int)
        self._conditionprob_var = collections.defaultdict(dict)


        for i in range(self._trainsetSize):
            self._S[self._train_y[i]] += len(self._train_x[i])
            self._word_num += len(self._train_x[i])
            for item in self._train_x[i]:
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

                    if (self._conditionprob_var[ck].has_key(xi) ):
                        prob *= self._conditionprob_var[ck][xi]
                    else:
                        prob *= 1.0*self._lambda/(self._S[ck]+len(self._worddic))#!!!!!!!!!!!!!!!!!!!!! not to modify
                prob *= self._prioriprob[ck]
                # print  ('sample:',test_x[i],' be',ck,'has ',prob,' probability')
                if (prob >= max_prob):
                    max_prob = prob
                    t_ck = ck
                prob = 1
            if (t_ck != ''):
                result.append(t_ck)

        return result
