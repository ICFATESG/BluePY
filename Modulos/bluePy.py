import bluetooth as bt
import json
import pprint
print("performing inquiry...")
mac=[]
mac4tr=["9C:5C:F9:66:73:34", "B8:A3:E0:72:9E:EA","00:E0:4C:2A:26:60","00:E0:4C:76:0A:A7","00:E0:4C:0D:C7:58","00:E0:4C:79:7A:17","00:E0:4C:07:72:D9","00:E0:4C:60:97:77"]
def varrer(adaptID):


        try:
            areInRange = bt.discover_devices(lookup_names=True,device_id=adaptID,duration=10)
            print (areInRange)
            for addr, name in areInRange:
                exist(addr)
                print (' %s  ->  %s' % (addr, name))
        except:
            areInRange = bt.discover_devices(lookup_names=True, device_id=adaptID, duration=10)

            for addr, name in areInRange:
                exist(addr)
                print (' %s  ->  %s' % (addr, name))




def exist(string):
    if string not in mac:
        mac.append(string)

def json_list(list):
    lst = []
    for pn in list:
        d = {}
        d['mac'] = pn
        lst.append(d)
    return json.dumps(lst)





#varrer(0)
