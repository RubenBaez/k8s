from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route("/service3")
def index():
    numero = request.args.get('numero', type=int, default=0.0)
    operadores = request.args.getlist('operadores')

    if 'suma' in operadores:
        numero = numero/10

    if 'div' in operadores:
        numero = numero / 10

    numeroRandom = random.uniform(1,10)


    return jsonify(data={
        'nombre':'microservicio 3',
        'numero':numeroRandom,
        'operadores':operadores
        })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)