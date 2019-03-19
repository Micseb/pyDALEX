# Keras sample model generation
#from sample_models import KerasExample
#(data, labels, model, names) = KerasExample().create_sample_model()

# Random forest sample model generation
# from sample_models import RandomForestExample
# (data, labels, model, names) = RandomForestExample().create_random_forest_model()

# Linear regression sample model generation
from sample_models import LinearRegressionExample
(data, labels, model, names) = LinearRegressionExample().create_sample_linear_regression()

# Creating input
from py_dalex_client import explain_request_model, model_down_request_model
explain_request = [explain_request_model.ExplainRequestModel(model, data, labels, names)]
model_down_request = model_down_request_model.ModelDownRequestModel(['model_performance', 'variable_importance'])

# Dalex operations
import py_dalex
website_link = py_dalex.py_dalex.generate_website(explain_request, model_down_request)
print(website_link)