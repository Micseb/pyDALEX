# Keras sample model generation
#from sample_models import KerasExample
#(data, labels, model, names) = KerasExample().create_sample_model()

# Random forest sample model generation
#from sample_models import RandomForestExample
#(data, labels, model, names) = RandomForestExample().create_random_forest_model()

# Linear regression sample model generation
from sample_models import LinearRegressionExample
(data, labels, model, names) = LinearRegressionExample().create_sample_linear_regression()

# Dalex operations
from py_dalex import py_dalex
explainer = py_dalex.explain(model, data, labels, names)
py_dalex.generate_website(explainer)