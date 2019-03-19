from flask import Flask
from flask import request
import py_dalex
import jsonpickle

# http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application
app = Flask(__name__)

@app.route('/modelDown', methods=['GET'])
def get_model_down():
    return 'Hello, World!'

@app.route('/modelDown', methods=['POST'])
def generate_model_down():
    explain_request = jsonpickle.decode(request.form['models'])
    model_down_request = jsonpickle.decode(request.form['website_options'])
    website_link = py_dalex.py_dalex.generate_website(explain_request, model_down_request)
    return website_link