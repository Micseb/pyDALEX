from flask import Flask
from flask import request
from py_dalex import py_dalex
import jsonpickle

# http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application
app = Flask(__name__)

@app.route('/modelDown', methods=['GET'])
def get_model_down():
    return 'Hello, World!'

@app.route('/modelDown', methods=['POST'])
def generate_model_down():
    model_data = request.form['model_data']
    model_data = jsonpickle.decode(model_data)
    explainer = py_dalex.explain(model_data['model'], model_data['data'], model_data['labels'], model_data['names'])
    py_dalex.generate_website([explainer])