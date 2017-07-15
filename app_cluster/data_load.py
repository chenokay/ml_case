#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

class DataManager:
    def __init__(self, file):
        self.fea_file = file

    def load_file(self):
        ## data format 
        ## feature_lines fea_number
        ## appid fea_type_name1   fea_type_name2  ...
        with open(self.fea_file, "r") as fd:
            lines, fea_count = fd.next().split(',') 
            data = np.empty(( int(lines), int(fea_count) ))
            target = np.empty( (int(lines), ) )
            fea_names = np.array(fd.next().strip().split(',')[1:])

            for i in xrange(int(lines)):
                line = fd.next()
                d = line.split(',')
                data[i] = np.asarray(d[1:], dtype=np.int)
                target[i] = np.asarray(d[0], dtype=np.int)

            self.X = data
            self.appid = target
            self.names = fea_names
