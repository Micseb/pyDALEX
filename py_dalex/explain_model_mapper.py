from .predict_function_generator import PredictFunctionGenerator
from .models.explain_model import ExplainModel
import rpy2.robjects as robjects

class ExplainModelMapper:
    def __init__(self):
        self._predict_function_generator = PredictFunctionGenerator()  

    def map(self, explain_request_model):
        predict_function = self._predict_function_generator.generate_function(explain_request_model.model)
        model = robjects.ListVector({})
        data = robjects.DataFrame({explain_request_model.column_names[x]:  robjects.FloatVector(explain_request_model.data[:,x]) for x in range(explain_request_model.data.shape[1])})
        y = explain_request_model.y
        link = explain_request_model.link
        label = explain_request_model.label or type(model).__name__
        return ExplainModel(model, data, y, predict_function, label, link)