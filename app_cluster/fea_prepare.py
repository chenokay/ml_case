#!/usr/bin/env python
# -*- coding: utf-8 -*-

def load_tag_dict(file):
    tag_dict = {}
    tag_vec = []
    with open(file, 'r') as fd:
        for line in fd:
            items = line.split('\t')
            if len(items) != 2:
                continue
            tag_dict[items[1].strip()] = 1

    for key, v in tag_dict.items():
        tag_vec.append(key)

    tag_vec.sort()
    tag_dict.clear()
    print '0',',',','.join(tag_vec)
    for i in xrange(len(tag_vec)):
        tag_dict[tag_vec[i]] = i
    return tag_dict

APPID2TAG = 'appid2tag'

if __name__ == '__main__':
    tag_dict = load_tag_dict(APPID2TAG)

    last_appid = ''

    fea_vec = ['0' for i in xrange(len(tag_dict))]
    with open(APPID2TAG, 'r') as fd:
        init = 0
        for line in fd:
            items = line.split('\t')
            if len(items) != 2:
                continue

            appid = items[0]
            tag_id = items[1].strip()
            if appid != last_appid and 1 == init:
                print last_appid,',',','.join(fea_vec)
                last_appid = appid
                fea_vec = ['0' for i in xrange(len(tag_dict))]
                fea_vec[tag_dict[tag_id]] = '1'
            elif appid != last_appid and 0 == init:
                last_appid = appid
                fea_vec = ['0' for i in xrange(len(tag_dict))]
                fea_vec[tag_dict[tag_id]] = '1'
            else:
                fea_vec[tag_dict[tag_id]] = '1'
            init = 1

        print last_appid,',',','.join(fea_vec)
