from flask import Flask
from flask import request
from py_dalex import py_dalex, ExplainModelMapper, ModelDownModelMapper
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

    explain_mapper = ExplainModelMapper()
    model_down_mapper = ModelDownModelMapper()

    explain_models = [explain_mapper.map(item) for item in explain_request]
    model_down_model = model_down_mapper.map(model_down_request, explain_request[0].column_names)

    explainers = py_dalex.generate_explainers(explain_models)
    website_link = py_dalex.generate_website(explainers, model_down_model)
    return website_link