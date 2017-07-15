#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from data_load import DataManager
from sklearn.metrics import silhouette_samples,silhouette_score

if __name__ == '__main__':

    dm = DataManager('fea_vec')
    dm.load_file()
    #print dm.X
    #print dm.appid
    #print dm.names

    random_state = 170

    range_n_clusters = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,  15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,  30, 40, 50, 60, 70, 80]
    for n_clusters in range_n_clusters:
        y_pred = KMeans(n_clusters=n_clusters, random_state=random_state).fit_predict(dm.X)
    #print y_pred

        silhouette_avg = silhouette_score(dm.X, y_pred)
        print("n_clusters = ", n_clusters, "the average silhouette_score is:", silhouette_avg)
    #l = len(dm.appid)
    #for i in xrange(l):
    #    print int(dm.appid[i]), y_pred[i]
