import json
import time
from datetime import datetime

def put(Obj):
    print Obj+' foi salvo no banco!'
    return ''

def get():
    print 'A lista de MACs foi retornada com sucesso!'
    return ''

def get(Obj):
    print 'O usuario que tem o MAC '+Obj+' foi retornado com sucesso!'
    return ''

def post(lista_de_MAC):
    for MAC in lista_de_MAC:
        now = datetime.now()
        usuario = get(lista_de_MAC)
        usr=json(usuario)
        dados=list(usr)
        dados[1].append('Aula de python')
        if len(dados) <= 2:
            #entrada
            dados[2].append(str(now.hour)+':'+str(now.minute))
        else:
            #saida
            dados[3].append(str(now.hour)+':'+str(now.minute))





put('Ronaldo')
