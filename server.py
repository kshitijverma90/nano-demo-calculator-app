from flask import Flask, make_response,request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    response=make_response("Hello world!",200)
    return response

@app.route("/calculator/add", methods=['POST'])
def add():
    variable_name=request.get_json()
    num1=variable_name['first']
    num2=variable_name['second']
    response=make_response({'result':num1+num2},200)
    return response

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    variable_name=request.get_json()
    num1=variable_name['first']
    num2=variable_name['second']
    response=make_response({'result':num1-num2},200)
    return response

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
