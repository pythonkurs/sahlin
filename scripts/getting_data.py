#!/usr/bin/env python
'''
Created on Jan 24, 2013

@author: ksahlin
'''
from sahlin.Lecture2 import GetNYTrainData,CalculateStatusRepair
xml_file = "http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml"
outages = GetNYTrainData(xml_file)
fFractionOfRepairs = CalculateStatusRepair(outages)
print 'Fraction of repairs:', fFractionOfRepairs

