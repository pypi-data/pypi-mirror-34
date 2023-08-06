import unittest
import numpy as np
from six.moves import xrange
from sklearn.metrics import pairwise_distances
from sklearn.datasets import(
    load_iris, load_digits, load_diabetes)
from numpy.testing import assert_array_almost_equal
from sklearn import neighbors

from utils import read_ARFF

from dml import(
    NCA,LDA,RCA,PCA,ANMM,kNN)


#data=load_iris()
#data=load_digits()
#
#X=data['data']
#y=data['target']

#X,y,m = read_ARFF("./data/sonar.arff",-1)
#X,y,m = read_ARFF("./data/wdbc.arff",0)
X,y,m = read_ARFF("./data/spambase-460.arff",-1)

n,d = X.shape

print "Data dimensions: ", n, d

#dml = NCA(max_iter=10)
#dml = LDA(thres = 0.95)
#dml = RCA()
#dml = PCA(thres = 0.95)
dml = ANMM()

dml.fit(X,y)

#knn = kNN(n_neighbors=3,dml_algorithm=dml)
#knn.fit(X,y)
#
#print "Before learning metric kNN score [Train]: ", knn.score_orig()
#print "After learning metric kNN score [Train]: ", knn.score()


