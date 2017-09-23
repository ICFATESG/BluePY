#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bluetooth as bt
import json
print '____________________________________________'
print("BLUEPY © BLUEME AMBIENT CONTROL MODULE")
print("REST API PROVIDER OF BLUETOOTH")
print("BLUEME TEAM")
print '-------------------------------------------'
print("https://github.com/yangoff")
print '-------------------------------------------'
print("https://github.com/jpaulo789b/")
print '____________________________________________'
mac=[]
mac4tr=[] # "9C:5C:F9:66:73:34", "B8:A3:E0:72:9E:EA","00:E0:4C:2A:26:60","00:E0:4C:76:0A:A7","00:E0:4C:0D:C7:58","00:E0:4C:79:7A:17","00:E0:4C:07:72:D9","00:E0:4C:60:97:77"]


    

def varrer(self):
    self.mac=[]
    try:
        areInRange = bt.discover_devices(lookup_names=True,device_id=0,duration=10)
        #print (areInRange)
        for addr, name in areInRange:
            exist(addr)
            print (' %s  ->  %s' % (addr, name))
    except:
        areInRange = bt.discover_devices(lookup_names=True, device_id=0, duration=10)
        for addr, name in areInRange:
            exist(addr)
            print (' %s  ->  %s' % (addr, name))
    
    lst = []
    for pn in mac:
        d = {}
        d['mac'] = pn
        lst.append(d)
    self.mac4tr = json.dumps(lst)
    print "Atualizou"
    print mac4tr


def exist(string):
    
        mac.append(string)


    