'''
Created on Jan 25, 2013

@author: ksahlin
'''


def NYTrainOutagesByRepairs():
    xml_file = "http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml"
    import untangle
    doc = untangle.parse(xml_file) #read in the XML file
    outages = doc.NYCOutages.outage # fetch the outages
    iRepairCount = 0
    iTotOutages = len(outages)
    for outage in outages:
        reason = outage.get_elements('reason')[0].cdata #get the reason from each outage
        if reason == 'REPAIR': iRepairCount += 1 
    print 'Fraction of outages caused by repairs:', iRepairCount / float(iTotOutages)


