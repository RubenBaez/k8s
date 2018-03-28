from flask import Flask, request, jsonify
from requests import get, post
import json
app = Flask(__name__)
@app.route("/suma")
def getData():
    #dataservice1 = get('http://172.17.22.82').content
    dataservice1 = get('http://172.18.0.2:8000/').content
    js1 = dataservice1.decode('utf8').replace("'",'"')
    datajson1 = json.loads(js1)

    #dataservice2 = get('http://172.17.22.82/service2').content
    dataservice2 = get('http://172.18.0.3:8001/service2').content
    js2 = dataservice2.decode('utf8').replace("'", '"')
    datajson2 = json.loads(js2)

    #dataservice3 = get('http://172.17.22.82/service3').content
    dataservice3 = get('http://172.18.0.4:8002/service3').content
    js3 = dataservice3.decode('utf8').replace("'", '"')
    datajson3 = json.loads(js3)

    a = suma(datajson1, datajson2, datajson3)
    return a

def suma(json1, json2, json3):
    numero1 = json1['data']['numero']
    numero2 = json2['data']['numero']
    numero3 = json3['data']['numero']
    suma = numero1 + numero2 + numero3
    cadena = 'servicio1 = ' + str(numero1) + '<br>servicio2 = ' + str(numero2) + '<br>servicio3 = ' + str(numero3) +'<br><br> Resultado = ' + str(suma)
    return str(cadena)

@app.route("/sumavalor")
def getDataEnviar():
    #dataservice1 = get('http://172.17.22.82').content
    dataservice1 = get('http://172.18.0.2:8000/').content
    js1 = dataservice1.decode('utf8').replace("'",'"')
    datajson1 = json.loads(js1)

    #dataservice2 = get('http://172.17.22.82/service2').content
    dataservice2 = get('http://172.18.0.3:8001/service2').content
    js2 = dataservice2.decode('utf8').replace("'", '"')
    datajson2 = json.loads(js2)

    #dataservice3 = get('http://172.17.22.82/service3').content
    dataservice3 = get('http://172.18.0.4:8002/service3').content
    js3 = dataservice3.decode('utf8').replace("'", '"')
    datajson3 = json.loads(js3)

    numero1 = datajson1['data']['numero']
    numero2 = datajson2['data']['numero']
    numero3 = datajson3['data']['numero']
    suma = numero1 + numero2 + numero3

    return jsonify(data={
        'name':'suma',
        'numero':suma
        })


if __name__=="__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)

