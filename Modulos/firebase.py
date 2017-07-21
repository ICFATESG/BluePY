import pyrebase as pyB
import pprint
from json import loads, dumps
from collections import OrderedDict
config = {
  "apiKey": "AIzaSyBrMKELe2ecLdCFAF1ojo16HwUMDAKsvMM",
  "authDomain": "blueme-3ac42.firebaseapp.com",
  "databaseURL": "https://blueme-3ac42.firebaseio.com",
  "storageBucket": "blueme-3ac42.appspot.com  "
}

fb = pyB.initialize_app(config)
auth = fb.auth()
db = fb.database()

users = db.child("Usuarios").get()
dictUser=users.val()


def to_dict(input_ordered_dict):
    return loads(dumps(input_ordered_dict))

printable=to_dict(dictUser)
#pprint.pprint(printable)
print type(printable)
#02:00:00:00:00:00