from scapy.all import *
from macVendorsExtractor import getMacVendors
from csvGenerator import graph1and2, graph3
import time

seconds = time.time()
devices = {}
ssids = []
PRCounter = 0
PNLCounter = 0
directPR = 0
broadcastPR = 0
nullableSSID = 0
macVendorsDict = getMacVendors()

pcapListFileNames = [
    'probes-2013-02-17.pcap1',
    'probes-2013-02-17.pcap2',
    'probes-2013-02-17.pcap3',
    'probes-2013-02-17.pcap4',
    'probes-2013-04-29.pcap1',
    'probes-2013-04-30.pcap1',
    'probes-2013-04-30.pcap2',
    'probes-2013-04-30.pcap3',
    'probes-2013-05-03.pcap1',
    'probes-2013-05-03.pcap2',
    'probes-2013-05-03.pcap3',
]


def verifyPCAP(pcap):
    global devices, PRCounter, directPR, broadcastPR, ssids, nullableSSID, macVendorsDict
    for pkt in pcap:
        PRCounter += 1
        if pkt.haslayer(Dot11):
            mac = pkt.addr2
            if mac not in devices:
                devices[mac] = {}
            
            macVendorAddress = mac.replace(':', '')[:6].upper()

            if (macVendorsDict.has_key(macVendorAddress)):
                devices[mac]['vendor'] = macVendorsDict[macVendorAddress]
            else:
                devices[mac]['vendor'] = 'N/E'


            if 'pnl' not in devices[mac]:
                devices[mac]['pnl'] = []

            try:
                ssid = pkt.info
            except:
                ssid = ''
                nullableSSID += 1

            if ssid == '':
                broadcastPR += 1
            else:
                directPR += 1

                if ssid not in ssids:
                    ssids.append(ssid)

                if ssid not in devices[mac]['pnl']:
                    devices[mac]['pnl'].append(ssid)


def countPNLs():
    global devices, PNLCounter
    for dev in devices.values():
        if len(dev['pnl']) > 0:
            PNLCounter += 1


def visualizeData(maxSize):
    global devices
    c = 0
    for mac, info in devices.iteritems():
        if c < maxSize:
            print "MAC: %s\nPNL: %s\nVendor: %s\n\n" %(mac, info['pnl'], info['vendor'])
        else:
            break
        c += 1


# SINGLE SCRIPT #
# to test, comment MASS SCRIPT
verifyPCAP(rdpcap(pcapListFileNames[0]))

# MASS SCRIPT #
# to test, comment SINGLE SCRIPT
# for pcap in pcapListFileNames:
#     print 'reading %s' % pcap
#     data = rdpcap(pcap)
#     print '%s read. Starting verification' % pcap
#     verifyPCAP(data)
#     print '%s verification finished sucessfully' % pcap

countPNLs()

# graph1and2(devices)

# graph3(devices)

#visualizeData(2000)

print "Probe requests: %d" % PRCounter
print "Direct probe requests: %d" % directPR
print "Broadcast probe requests: %d" % broadcastPR
print "Device count: %d" % len(devices.keys())
print "SSIDs count: %d" % len(ssids)
print "Nullable SSIDs count: %d" % nullableSSID
print "PNL count: %d" % PNLCounter

# Adamic-Adar
from adamicAdar import criaGrafo, geraSimilaridade, plotG
grafo = criaGrafo(devices)
geraSimilaridade(grafo)
plotG(grafo)

print "Approximate Runtime: %d minutes" % ((time.time() - seconds) // 60)

"""
Resultado para o probes-2013-02-17.pcap1:
Probe requests: 18597
Direct probe requests: 9849
Broadcast probe requests: 8748
Device count: 1749
SSIDs count: 2184
Nullable SSIDs count: 0
PNL count: 576

#Resultado para todos os probes
Probe requests: 376117
Direct probe requests: 198589
Broadcast probe requests: 177528
Device count: 14641
SSIDs count: 19126
Nullable SSIDs count: 5
PNL count: 5388
Approximate Runtime: 9 minutes
"""
