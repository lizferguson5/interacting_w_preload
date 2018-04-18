#! /usr/local/bin/python
# -*- coding: utf-8 -*-

import codecs
import chardet
import pandas as pd


target_file = codecs.open('/Users/leila/Documents/OOI_GitHub_repo/work/002database/preload_ParameterDefs_data.csv', 'w','utf-8')

url = 'https://raw.githubusercontent.com/oceanobservatories/preload-database/master/csv/ParameterDefs.csv'
preload_data = pd.read_csv(url)


tunit = '/Users/leila/Documents/OOI_GitHub_repo/work/002database/test.csv'


tu = pd.read_csv(tunit)
for i in range(len(tu['_Unit'])):
    preload_data = preload_data.replace(tu['_Unit'][i],'ºC',regex=True)


preload_data.to_csv('/Users/leila/Documents/OOI_GitHub_repo/work/002database/preload_ParameterDefs_data.csv', index=False)