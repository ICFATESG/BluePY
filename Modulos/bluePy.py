import bluetooth as bt

print("performing inquiry...")

def varrer(adaptID):
    SAIR = True
    volta=1
    while SAIR == True:


        print ('volta ' + str(volta))
        try:
            areInRange = bt.discover_devices(lookup_names=True,device_id=adaptID,duration=10)
        except:
            pass
        volta=volta+1
        print ('Found %d devices' % len(areInRange))
        for addr, name in areInRange:
            print (' %s  ->  %s' % (addr,name))





varrer(0)