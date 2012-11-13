from mongoengine import Document, StringField, FloatField, IntField
from mongoengine import DateTimeField, BooleanField
from datetime import datetime

class TestAcumuladores(Document):
    operario = IntField(required=True)
    fecha = DateTimeField(default=datetime.now)
    of = StringField(required=True)
    peso = FloatField(required=True)
    volumen = FloatField(required=True)
    resultado = BooleanField(required=True)

    meta = {
        'ordering': ['-fecha']
    }

    def __unicode__(self):
        datos = "\n"
        datos += "Operario :" + self.operario + "\n"
        datos += "OF       :" + self.of + "\n"
        datos += "Fecha    :" + str(self.fecha) + "\n"
        datos += "Peso     :" + str(self.peso) + "\n"
        datos += "Volumen  :" + str(self.volumen) + "\n"
        datos += "Resultado:" + str(self.resultado) + "\n"
        return datos

    def testear(self):
        dato = (self.peso / self.volumen) * 1000
        if (dato >= 35 and dato <= 60):
            self.resultado = True
        else:
            self.resultado = False
