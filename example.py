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
from pyDalex import PyDalex
pyDalex = PyDalex()

explainer = pyDalex.explain(model, data, labels, names)
pyDalex.generate_website(model)