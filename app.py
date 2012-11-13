from flask import Flask
from flask import flash
from flask import render_template
from flask import request
from test import TestAcumuladores
from mongoengine import connect
import logging


app = Flask(__name__)
app.debug = True


file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.secret_key = 'Testeo acumuladoresdsfdfdkjfsjgdjhfkjljkl'
connect("test1")

@app.route("/")
def index():
    return render_template("hello.html")

def validarDatosAcumuladores(request, test):
    error = False
    operario = 0
    of = ""
    peso = 0.0
    volumen = 0.0
    try:
        operario = request.form['operario']
        of = request.form['of']
        peso = float(request.form['peso'])
        volumen = float(request.form['volumen'])
    except:
        flash("Error recogiendo datos")
        error = True

    if len(str(operario)) != 4:
        flash("Operario no valido", 'error')
        error = True
    if len(of) != 9:
        flash("OF no valida", 'error')
        error = True
    if peso == 0:
        flash("Peso no valido", 'error')
        error = True
    if volumen == 0:
        flash("Volumen no valido", 'error')
        error = True

    test.operario = operario
    test.of = of
    test.peso = peso
    test.volumen = volumen
    return not error


@app.route("/Acumuladores", methods=['GET', 'POST'])
def testAcumuladores():
    app.logger.info("TESTEAR ACUMULADORES")
    if request.method == 'GET':
        app.logger.info("\tGET")
        return render_template("TestAcumuladores.html")
    else:
        app.logger.info("\tPOST")
        test = TestAcumuladores()
        if validarDatosAcumuladores(request, test):
            app.logger.info("\tDATOS VALIDOS")
            test.testear()
            app.logger.info(test)
            test.save()
        return render_template("TestAcumuladores.html", test=test)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
