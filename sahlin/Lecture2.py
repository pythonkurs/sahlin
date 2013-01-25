'''
Created on Jan 25, 2013

@author: ksahlin
'''


def GetNYTrainData(xml_file):
    import untangle
    doc = untangle.parse(xml_file) #read in the XML file
    outages = doc.NYCOutages.outage # fetch the outages
    return(outages)

def CalculateStatusRepair(outages):
    iRepairCount = 0
    iTotOutages = len(outages)
    for outage in outages:
        reason = outage.get_elements('reason')[0].cdata #get the reason from each outage
        if reason == 'REPAIR': iRepairCount += 1 
    return( iRepairCount / float(iTotOutages) )

