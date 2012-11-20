from test import TestAcumuladores
from mongoengine import connect
from pprint import pprint
import json

connect("test1")
datos = TestAcumuladores.objects.all()

import ipdb; ipdb.set_trace() # BREAKPOINT

lista = []
for dato in datos:
    lista.append(dato.to_dict())

print lista
pprint(json.dumps(lista))
