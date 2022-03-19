# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:20:56 2019

@author: Ahmed Tarek
"""

import numpy as np
from sklearn.metrics import f1_score
from sklearn.neural_network import MLPClassifier
import pandas as pd
from tabulate import tabulate
import pickle 
from sklearn import svm
from sklearn.svm import SVC 
from sklearn.metrics import classification_report, confusion_matrix  
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

pca = pickle.load(open('PCA.sav','rb'))
mlp = pickle.load(open('mlp_classifier.sav','rb'))


#test_target = np.concatenate((freq2_target,freq3_target,freq4_target,freq5_target,freq6_target),axis = 0)
#test_features = np.concatenate((freq2_features,freq3_features,freq4_features,freq5_features,freq6_features),axis = 0)

features= pca.transform(features)

dataset = np.concatenate((features, target),axis = 1)

XX = dataset[:,0: np.size(dataset,1)-1]
YY = np.transpose(dataset[: ,np.size(dataset,1) -1])
#x_train,x_test, y_train, y_test=train_test_split(XX,YY,test_size=0.99)

y_pred_MLP = mlp.predict(XX)
print ("***************SVM****************")
print(confusion_matrix(YY, y_pred_MLP))
print(classification_report(YY, y_pred_MLP))
F1_MLP = f1_score(YY, y_pred_MLP, average='macro')
