def graph1and2(devices):
    data = {}
    for mac, info in devices.iteritems():
        vendor = info['vendor']
        if vendor not in data:
            data[vendor] = {}
            data[vendor]['qtde'] = 1
        else:
            data[vendor]['qtde']+= 1
        
        if len(info['pnl']) > 0:
            if data[vendor].has_key('pnlExposed') is False:
                data[vendor]['pnlExposed'] = 1
            else:
                data[vendor]['pnlExposed'] += 1

    
    file = open('figure1and2.csv', 'w')
    file.write('vendors;qtde;qtdePNLExposed\n')

    for vendor, info in data.iteritems():
        if info.has_key('pnlExposed') is False:
            info['pnlExposed'] = 0
        file.write('%s;%d;%d\n' % (vendor, info['qtde'], info['pnlExposed']))
    
    file.close()
    print '\nFigure1 and Figure2 CSV generated\n'

def graph3(devices):
    data = {}
    for mac, info in devices.iteritems():
        for ssid in info['pnl']:
            if ssid not in data:
                data[ssid] = 1
            else:
                data[ssid] += 1
    
    file = open('figure3.csv', 'w')
    file.write('ssid;N devices\n')
    
    for ssid, qtde in data.iteritems():
        file.write('%s;%d\n' % (ssid, qtde))
    
    file.close()
    print '\nFigure3 CSV generated\n'
