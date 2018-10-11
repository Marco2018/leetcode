#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn import svm
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import StratifiedKFold, StratifiedShuffleSplit


# In[2]:


import sys, time

class ProgressBar:
    def __init__(self, count = 0, total = 0, width = 50):
        self.count = count
        self.total = total
        self.width = width
    def move(self):
        self.count += 1
    def log(self, s, sep="\n"):
        sys.stdout.write(' ' * (self.width + 9) + '\r')
        sys.stdout.flush()
        print(s, end=sep)
        progress = self.width * self.count / self.total
        sys.stdout.write('{0:3}/{1:3}: '.format(self.count, self.total))
        sys.stdout.write('#' * int(progress) + '-' * int(self.width - progress) + '\r')
        if progress == self.width:
            sys.stdout.write('\n')
        sys.stdout.flush()


# In[3]:


data_dir = '/home/taokun/data/mlcourse/Assignment01_SpeechDetection/'
train_data_dir = data_dir+'./training.data'
test_data_dir = data_dir+'testing.data'


# In[4]:


def read_data(train_data_dir, test_data_dir):
    train_set = np.array(pd.read_csv(train_data_dir, sep="\s+"))
    test_data = np.array(pd.read_csv(test_data_dir, sep="\s+"))
    num_train, data_dim = train_set.shape
    data_dim = data_dim - 1
    train_data = train_set[:, :data_dim]
    train_label = train_set[:, data_dim]
    return train_data, train_label, test_data


# In[5]:


def preprocess_data(train_data, test_data):
    max_value = np.max(train_data, axis = 0)
    min_value = np.min(train_data, axis = 0)
    middle_value = (max_value + min_value)/2
    scale = middle_value - min_value
    
    train_data = (train_data - middle_value)/scale
    test_data = (test_data - middle_value)/scale
    return train_data, test_data


# In[6]:


train_data, y_train, test_data = read_data(train_data_dir, test_data_dir)
X_train, X_test = preprocess_data(train_data, test_data)
C_lst = np.logspace(-2, 3, num=10, base=10)
gamma_lst = np.logspace(-1, 3, num=10,  base=10)
num_train = X_train.shape[0]


# In[7]:


sel_num = num_train
full_X_train = X_train
full_y_train = y_train
choice_index = np.random.choice(num_train, sel_num)
X_train = full_X_train[choice_index]
y_train = full_y_train[choice_index]


# In[8]:


import time

skf = StratifiedKFold(n_splits=5, shuffle=True)
train_accs = {}
valid_accs = {}
bar = ProgressBar(total=C_lst.shape[0]*gamma_lst.shape[0]*5)
for C in C_lst:
    for gamma in gamma_lst:
        clf = svm.SVC(C=C, gamma=gamma)
        train_acc_epoch = []
        valid_acc_epoch = []
        for train_index, valid_index in skf.split(X_train, y_train):
            start_time = time.time()
            X_t, X_v = X_train[train_index], X_train[valid_index]
            y_t, y_v = y_train[train_index], y_train[valid_index]
            clf.fit(X_t, y_t)
            train_accurate = np.mean(clf.predict(X_t) == y_t)
            valid_accurate = np.mean(clf.predict(X_v) == y_v)
            train_acc_epoch.append(train_accurate)
            valid_acc_epoch.append(valid_accurate)
            end_time = time.time()
            bar.move()
            bar.log(end_time-start_time, sep="")
        train_accs[(C, gamma)] = np.mean(train_acc_epoch)
        valid_accs[(C, gamma)] = np.mean(valid_acc_epoch)
accs = [train_accs, valid_accs]


# In[9]:


#scores = np.array(list(valid_accs.values()))
#xx, yy = np.meshgrid(C_lst, gamma_lst)
#scores = scores.reshape(xx.shape)
#plt.figure(figsize=(15, 15))
#plt.imshow(scores, cmap=plt.cm.hot)
#plt.colorbar()
#plt.xticks(np.arange(C_lst.shape[0]), np.log10(C_lst), rotation=45)
#plt.yticks(np.arange(gamma_lst.shape[0]), np.log10(gamma_lst))
#plt.show()


# In[10]:


import pickle
f = open("./accs.txt", "wb")
pickle.dump(obj=accs, file=f)
f.close()


# In[ ]:




