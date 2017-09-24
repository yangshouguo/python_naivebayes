
import numpy
from naiveBayes_textclass import NaiveBayes

class Reader():

    def __init__(self):
        self._trainx = []
        self._trainy = []
        self._allFeature = set()
        self._feature_size = 0

    def read(self,filename):



        file = open(filename)

        if file :
            lines = file.readlines()
            for line in lines:
                line_list = line.split('\t')
                feature = line_list[1].split(' ')
                feature_set = set(feature)

                self._allFeature = self._allFeature | (feature_set)
            self._allFeature = list(self._allFeature)
            self._feature_size = len(self._allFeature)

            i = 0
            for line in lines:
                self._trainx.append([0 for j in range(self._feature_size)])
                line_list = line.split('\t')
                tag = line_list[0]
                self._trainy.append(tag)
                features = line_list[1].split(' ')
                for item in features:
                    index = self._allFeature.index(item)
                    self._trainx[i][index] += 1
                i += 1

            return self._trainx,self._trainy,self._allFeature,self._feature_size

    def read_dic(self,filename):



        file = open(filename)

        if file :
            lines = file.readlines()
            i = 0
            for line in lines:
                self._trainx.append({})
                line_list = line.split('\t')
                tag = line_list[0]
                self._trainy.append(tag)
                features = line_list[1].split(' ')
                features = features[:len(features)-1]
                for item in features:
                    if self._trainx[i].has_key(item):
                        self._trainx[i][item] += 1
                    else:
                        self._trainx[i].update({item:1})
                i += 1

            return self._trainx,self._trainy




