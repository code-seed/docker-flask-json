import json

from flask import Flask
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/data')
def data():
    q_json = request.args.get('q')
    q_dict = json.loads(q_json)
    result_dict = get_result(q_dict)

    return jsonify(result_dict)    

def get_result(param_dict):
    result_dict = {}
    result_dict['result'] = "Hello {0}!".format(param_dict['name'])    

    return result_dict

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)