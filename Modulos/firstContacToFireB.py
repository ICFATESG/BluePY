'''
from firebase import firebase as fb
import pprint
resp=''
def manda_na_tela(st):
    print ('Imprime esta porra'+ str(st))
    print 'tete'

fb = fb.FirebaseApplication('https://primeirocontatofirebase.firebaseio.com/', None)

#resp = firebase.get('/users',None)
novodado='abrovsk'
resp=fb.post('/users',novodado)
'''

