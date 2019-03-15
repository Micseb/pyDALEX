import requests as requests
import jsonpickle 

from sample_models.LinearRegressionExample import LinearRegressionExample
(data, labels, model, names) = LinearRegressionExample().create_sample_linear_regression()

from py_dalex_client import explain_request_model, model_down_request_model
explain_request = explain_request_model.ExplainRequestModel(model, data, labels, names)
model_down_request = model_down_request_model.ModelDownRequestModel(['model_performance', 'variable_importance'])

address = 'http://127.0.0.1:5000/modelDown'
body = {'models': jsonpickle.encode([explain_request]), 'website_options': jsonpickle.encode(model_down_request)}
r = requests.post(address, data = body)