import os
from flask import Flask, jsonify
from flask_cors import CORS
from math import sqrt

app = Flask(__name__)

CORS(app)

app.config['JSON_AS_ASCII'] = False

# ----------------------------------------------------------------------------------------------------------------------

@app.route('/')
def root():
    return '<center><b>Copie e cole na barra de endereço, a operação que deseja fazer entre as opções abaixo: </b><br>' + \
           '------------------------------------------------------------------------------------------------------------------- <br>' + \
           'https://dsdtrabalho-gustavo.herokuapp.com/somar/digite 1ºvalor/digite 2ºvalor <br>' + \
           '------------------------------------------------------------------------------------------------------------------- <br>' + \
           'https://dsdtrabalho-gustavo.herokuapp.com/subtrair/digite 1ºvalor/digite 2ºvalor <br>' + \
           '------------------------------------------------------------------------------------------------------------------- <br>' + \
           'https://dsdtrabalho-gustavo.herokuapp.com/dividir/digite 1ºvalor/digite 2ºvalor <br>' + \
           '------------------------------------------------------------------------------------------------------------------- <br>' + \
           'https://dsdtrabalho-gustavo.herokuapp.com/multiplicar/digite 1ºvalor/digite 2ºvalor <br>' + \
           '------------------------------------------------------------------------------------------------------------------- <br>' + \
           'https://dsdtrabalho-gustavo.herokuapp.com/raizQuadrada/digite o valor <br>' + \
           '------------------------------------------------------------------------------------------------------------------- <br>' + \
           'https://dsdtrabalho-gustavo.herokuapp.com/potencia/base/expoente <br>' + \
           '------------------------------------------------------------------------------------------------------------------- <br>' + \
           'https://dsdtrabalho-gustavo.herokuapp.com/mediaAritmetica/1ºvalor;2ºvalor;3ºvalor;... <br>' + \
           '------------------------------------------------------------------------------------------------------------------- <br>' + \
           'https://dsdtrabalho-gustavo.herokuapp.com/mediaHarmonica/1ºvalor;2ºvalor;3ºvalor;... <br>' + \
           '------------------------------------------------------------------------------------------------------------------- <br>' + \
           'https://dsdtrabalho-gustavo.herokuapp.com/mod/1ºvalor;2ºvalor;3ºvalor;... <br>' + \
           '------------------------------------------------------------------------------------------------------------------- <br>'
# ----------------------------------------------------------------------------------------------------------------------


@app.route('/somar/<value1>/<value2>', methods=['GET'])
def somar(value1, value2):

    try:
        valor1 = int(value1)
    except:
        return 'Entre com o primeiro valor correto, valor invalido.'

    try:
        valor2 = int(value2)
    except:
        return 'Entre com o segundo valor correto, valor invalido.'

    ret = {"Resultado": valor1 + valor2}

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/subtrair/<value1>/<value2>', methods=['GET'])
def subtraction(value1, value2):
    try:
        valor1 = int(value1)
    except:
        return 'Entre com o primeiro valor correto, valor invalido.'

    try:
        valor2 = int(value2)
    except:
        return 'Entre com o segundo valor correto, valor invalido.'

    ret = {"Resultado": valor1 - valor2}

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/dividir/<value1>/<value2>', methods=['GET'])
def division(value1, value2):
    try:
        valor1 = int(value1)
    except:
        return 'Entre com o primeiro valor correto, valor invalido.'

    try:
        valor2 = int(value2)
    except:
        return 'Entre com o segundo valor correto, valor invalido.'

    try:
        ret = {"Resultado": valor1 / valor2}
    except ZeroDivisionError:
        return 'Divisão por zero não é possível'

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/multiplicar/<value1>/<value2>', methods=['GET'])
def multiplication(value1, value2):
    try:
        valor1 = int(value1)
    except:
        return 'Entre com o primeiro valor correto, valor invalido.'

    try:
        valor2 = int(value2)
    except:
        return 'Entre com o segundo valor correto, valor invalido.'

    ret = {"Resultado": valor1 * valor2}

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/raizQuadrada/<value>', methods=['GET'])
def squareroot(value):
    try:
        valor1 = int(value)
    except:
        return 'Entre com um valor de raiz quadrada correto, valor invalido.'

    ret = {"Resultado": sqrt(valor1)}

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/potencia/<base>/<exponent>', methods=['GET'])
def power(base, exponent):
    try:
        li_base = int(base)
    except:
        return 'Entre com um valor Base correto, valor invalido.'

    try:
        li_exponent = int(exponent)
    except:
        return 'Expoente inválido.'

    ret = {"Resultado": li_base ** li_exponent}

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/mediaAritmetica/<value1>', methods=['GET'])
def arithmeticaverage(value1):

    try:
        array = [float(numeros) for numeros in value1.split(';')]
    except:
        return 'A sequencia deve possuir somente números.'

    ret = {"Resultado": sum(array) / len(array)}

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/mediaHarmonica/<value1>', methods=['GET'])
def harmonicmean(value1):

    try:
        array = [1 / int(numeros) for numeros in value1.split(';')]
    except:
        return 'A sequencia deve possuir somente números.'


    ret = {"Resultado": len(array) / sum(array)}

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/mod/<value1>', methods=['GET'])
def mod(value1):

    dicionario = {}

    try:
        array = [int(numeros) for numeros in value1.split(';')]
    except:
        return 'A sequencia deve possuir somente números.'

    for numeros in array:
        try:
            dicionario[numeros] = dicionario[numeros] + 1
        except:
            dicionario[numeros] = 1

    ret = {"Resultado": [numero for numero, repeticoes in dicionario.items() if repeticoes == max(dicionario.values())]}

    return jsonify(ret)


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
