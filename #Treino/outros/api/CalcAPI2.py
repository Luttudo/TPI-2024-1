from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])

def calculadora():
    data = request.get_json()
    num1 = float(data["num1"])
    num2 = float(data["num2"])
    oper = data["oper"]

    if oper == "adc":
        result = num1 + num2
    
    elif oper == "sub":
        result = num1 - num2

    elif oper == "mul":
        result = num1 * num2
    
    elif oper == "div":
        result = num1 - num2
