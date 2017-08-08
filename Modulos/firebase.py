import xmlrpclib

import pyrebase as pyB
import pprint
from json import loads, dumps
import  json
from collections import OrderedDict
from xml.dom.minidom import parseString
config = {
  "apiKey": "AIzaSyDmOaIOhzHfD36CIwqghdq3oGPVvIgVqVY",
  "authDomain": "lueme-3acca.firebaseapp.com",
  "databaseURL": "https://blueme-3acca.firebaseio.com",
  "storageBucket": "blueme-3acca.appspot.com"
}
fb = pyB.initialize_app(config)
auth = fb.auth()
db = fb.database()
def pesquisaMaisFunda(jeison):
    for idx, val in enumerate(jeison):
        return str(val)

def to_dict(input_ordered_dict):
    return loads(dumps(input_ordered_dict))

def getToOneChild(path):
    users = db.child(path).get()
    dictUser = users.val()
    #   print type(dictUser) OrderedDict
    jsn = json.dumps(dictUser)
    #   print type(jsn) Str
    jeison = json.loads(jsn)
    #   print type(jeison) Dict
    return jsn


def bar(somejson, key,value):
    def val(node):
        # Searches for the next Element Node containing Value
        e = node.nextSibling
        while e and e.nodeType != e.ELEMENT_NODE:
            e = e.nextSibling
        return (e.getElementsByTagName('string')[0].firstChild.nodeValue if e
                else None)
    # parse the JSON as XML
    foo_dom = parseString(xmlrpclib.dumps((json.loads(somejson),)))
    # and then search all the name tags which are P1's
    # and use the val user function to get the value
    return [val(node) for node in foo_dom.getElementsByTagName('name')
            if node.firstChild.nodeValue in key and node.firstChild.nodeValue==value]






dicty = getToOneChild("Usuarios")
#/2AF6khBTAPSTRra9dYlqyJKr38R2/OficinaVisitada
pprint.pprint(dicty)
print(bar(dicty,'mac','38:A4:ED:8D:7F:5B'))





