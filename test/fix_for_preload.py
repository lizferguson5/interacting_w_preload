#! /usr/local/bin/python
# -*- coding: utf-8 -*-

import codecs
import pandas as pd


target_file = codecs.open('/Users/leila/Documents/OOI_GitHub_repo/work/002database/preload_ParameterDefs_data.csv', 'w','utf-8')

preload_data = pd.read_csv('https://raw.githubusercontent.com/oceanobservatories/preload-database/master/csv/ParameterDefs.csv')

unit_2_change = '/Users/leila/Documents/OOI_GitHub_repo/work/002database/test.csv'

unit_preferred = 'ºC'

tu = pd.read_csv(unit_2_change)
for i in range(len(tu['_Unit'])):
    preload_data = preload_data.replace(tu['_Unit'][i], unit_preferred,regex=True)


preload_data.to_csv('/Users/leila/Documents/OOI_GitHub_repo/work/002database/preload_ParameterDefs_data.csv', index=False)