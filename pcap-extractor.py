from scapy.all import *
from macVendorsExtractor import getMacVendors

devices = {}
ssids = []
PRCounter = 0
PNLCounter = 0
directPR = 0
broadcastPR = 0
macVendorsDict = getMacVendors()

pcapListFileNames = [
    'probes-2013-02-17.pcap1',
    'probes-2013-02-17.pcap2',
    'probes-2013-02-17.pcap3',
    'probes-2013-02-17.pcap4',
    'probes-2013-04-29.pcap1',
    'probes-2013-04-29.pcap2',
    'probes-2013-04-29.pcap3',
    'probes-2013-05-03.pcap1',
    'probes-2013-05-03.pcap2',
    'probes-2013-05-03.pcap3',
]


def verifyPCAP(pcap):
    global devices, PRCounter, directPR, broadcastPR, ssids, macVendorsDict
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

            ssid = pkt.info

            if ssid == '':
                broadcastPR += 1
            else:
                directPR += 1

                if ssid not in ssids:
                    ssids.append(ssids)

                if ssid not in devices[mac]['pnl']:
                    devices[mac]['pnl'].append(ssid)


def countPNLs():
    global devices, PNLCounter
    for dev in devices.values():
        if len(dev['pnl']) > 0:
            PNLCounter += 1


def visualizeData():
    global devices
    c = 0
    for mac, info in devices.iteritems():
        if c < 10:
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
#     data = rdpcap(pcap)
#     verifyPCAP(data)

countPNLs()

# visualizeData()

print "Probe requests: %d" % PRCounter
print "Direct probe requests: %d" % directPR
print "Broadcast probe requests: %d" % broadcastPR
print "Device count: %d" % len(devices.keys())
print "SSIDs count: %d" % len(ssids)
print "PNL count: %d" % PNLCounter
