from flask import Flask, request, jsonify
import random

app = Flask(__name__)
#app.config['DEBUG'] = True

@app.route("/")
def ruben():

    numero = request.args.get('numero', type=int, default=0.0)
    operadores = request.args.getlist('operadores')

    #error que no existe un operador  

    if 'suma' in operadores:
        numero = numero * 10
    #else:
        #return jsonify(data={'error': 'No se encuentra el operador'})

    if 'mult' in operadores:
        numero = numero * 100

    numerorandom = random.uniform(1,5)
    numero = numero * numerorandom
    #return str(numero)
    return jsonify(data={
        'nombre':'microservicio 1',
        'numero':numerorandom,
        'operadores':operadores
        })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
