from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route("/service4")
def service():
    numeroRandom = random.uniform(10,100)
    nombre = 'microservicio 4'

    return jsonify(data={
        'nombre':nombre,
        'numero':numeroRandom,
        'operadores': 'factorial'
        })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=6000, debug=True)