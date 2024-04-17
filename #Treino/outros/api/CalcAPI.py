from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])

def calculator():
    data = request.get_json()
    num1 = float(data["num1"])
    num2 = float(data["num2"])
    oper = data["operation"]

    if oper == "add":
        result = num1 + num2

    elif oper == "subtract":
        result = num1 - num2

    elif oper == "multiply":
        result = num1 * num2

    elif oper == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Não dividirás por zero"

    return {"Result": result}

if __name__ == "__main__":
    app.run(debug=True)
    

