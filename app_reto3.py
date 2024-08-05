from flask import Flask, jsonify, request

app = Flask(__name__)


def ulam(numero):
    valor = numero
    lista=[]
    while(valor > 1):
        if(valor % 2 == 0):
            valor =(valor/2)
            lista.append(valor)
        else:
            valor = (valor * 3) + 1
            lista.append(valor)
    return lista
    
@app.route('/ulam', methods = ['POST'])
def serie_ulam():
    data = request.get_json()
    input_numero=data.get('numero')
    result = ulam(input_numero)
        
    return jsonify({"Serie": result})


if __name__ == '__main__':
    app.run(debug=False)