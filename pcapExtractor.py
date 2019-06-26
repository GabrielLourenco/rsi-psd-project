from scapy.all import *
from scapy.layers.dot11 import Dot11
from macVendorsExtractor import getMacVendors
from csvGenerator import graph1and2, graph3
from kafkaProducer import sendToSpark
import time
from tbIntegration import turnLedOn

seconds = time.time()
devices = {}
ssids = []
PRCounter = 0
PNLCounter = 0
directPR = 0
broadcastPR = 0
nullableSSID = 0
macVendorsDict = getMacVendors()
pcapCount = 0
accelerateFactor = 100

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
    global devices, PRCounter, directPR, broadcastPR, ssids, nullableSSID, macVendorsDict, pcapCount, accelerateFactor
    pcapCount += 1
    turnLedOn(pcapCount)
    demanda = None

    for pkt in pcap:
        PRCounter += 1
        if pkt.haslayer(Dot11):
            timestamp = pkt.time
            if demanda is None:
                demanda = time.time() - timestamp
                timestampIni = timestamp

            currentTime = time.time() - demanda

            while timestamp > timestampIni + (currentTime - timestampIni) * accelerateFactor:
                currentTime = time.time() - demanda

            mac = pkt.addr2
            try:
                ssid = pkt.info.decode("utf-8")
                if ssid == '':
                    ssid = 'BROADCAST'
            except:
                ssid = 'NULL'

            macVendorAddress = mac.replace(':', '')[:6].upper()
            
            if (macVendorsDict.get(macVendorAddress)):
                vendor = macVendorsDict[macVendorAddress]
            else:
                vendor = 'N/E'


            sendToSpark(mac, vendor, timestamp, ssid)


def countPNLs():
    global devices, PNLCounter
    for dev in devices.values():
        if len(dev['pnl']) > 0:
            PNLCounter += 1


# SINGLE SCRIPT #
# to test, comment MASS SCRIPT
print('reading pcap')
verifyPCAP(rdpcap(pcapListFileNames[0]))

# MASS SCRIPT #
# to test, comment SINGLE SCRIPT
# for pcap in pcapListFileNames:
#     print 'reading %s' % pcap
#     data = rdpcap(pcap)
#     print '%s read. Starting verification' % pcap
#     verifyPCAP(data)
#     print '%s verification finished sucessfully' % pcap

# countPNLs()

# graph1and2(devices)

# graph3(devices)

# visualizeData(10)

# print ("Probe requests: %d" % PRCounter)
# print ("Direct probe requests: %d" % directPR)
# print ("Broadcast probe requests: %d" % broadcastPR)
# print ("Device count: %d" % len(devices.keys()))
# print ("SSIDs count: %d" % len(ssids))
# print ("Nullable SSIDs count: %d" % nullableSSID)
# print ("PNL count: %d" % PNLCounter)

# Adamic-Adar
# from academicAdar import criaGrafo, runTeste
# grafo = criaGrafo(devices)
# runTeste(grafo)

print ("Approximate Runtime: %f s" % (time.time() - seconds))
