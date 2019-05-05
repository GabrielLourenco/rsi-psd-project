def getMacVendors():
    vendors = {}
    arq = open('mac-vendor.txt', 'r')
    lines = arq.readlines()

    for macVendor in lines:
        info = macVendor.split('\t')
        vendors[info[0]] = info[1].replace('\n', '')

    arq.close()
    return vendors
