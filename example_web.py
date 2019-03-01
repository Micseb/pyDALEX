import requests as requests
import jsonpickle 

from sample_models.LinearRegressionExample import LinearRegressionExample
(data, labels, model, names) = LinearRegressionExample().create_sample_linear_regression()

address = 'http://127.0.0.1:5000/modelDown'
body = {'model_data': jsonpickle.encode({'model': model, 'data': data, 'labels': labels, 'names': names})}
r = requests.post(address, data = body)