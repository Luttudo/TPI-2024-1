from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculadora', methods=['POST'])
def calculadora():
    data = request.get_json()

    num1 = data['num1']
    num2 = data['num2']

    operacao = data['operacao']

    if operacao == 'adicao':
        resultado = num1 + num2
    elif operacao == 'subtracao':
        resultado = num1 - num2
    elif operacao == 'multiplicacao':
        resultado = num1 * num2
    elif operacao == 'divisao':
        resultado = num1 / num2
    else:
        return jsonify({'error': 'Operação inválida'})

    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run()


