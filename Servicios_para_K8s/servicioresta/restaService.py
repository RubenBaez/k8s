from flask import Flask, request, jsonify
from requests import get
import json
app = Flask(__name__)

@app.route("/resta")
def getData():

    #dataservicesuma = get('http://172.17.22.82/sumavalor').content
    dataservicesuma = get('http://192.168.99.101/sumavalor').content
    jssum = dataservicesuma.decode('utf8').replace("'",'"')
    datajsonsuma = json.loads(jssum)

    #dataservice4 = get('http://172.17.22.82/service4').content
    dataservice4 = get('http://192.168.99.101/service4').content
    js4 = dataservice4.decode('utf8').replace("'",'"')
    datajson4 = json.loads(js4)

    a = resta(datajsonsuma, datajson4)

    return a

def resta(json1 , json2):
    numero1 = json1['data']['numero']
    numero2 = json2['data']['numero']
    resta = numero1 - numero2
    cadena = 'la suma de todos es = ' + str(numero1) + '<br>servicio4 = ' + str(numero2) + '<br>la resta es = ' + str(resta)
    return cadena

if __name__=="__main__":
    app.run(host="127.0.0.1", port=5002, debug=True)
