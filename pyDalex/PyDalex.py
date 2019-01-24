import rpy2.robjects as robjects
import rpy2.rinterface as rinterface
import rpy2.robjects.numpy2ri as numpy2ri
from rpy2.robjects.packages import importr
from .PredictFunctionGenerator import PredictFunctionGenerator

class PyDalex:  
    def __init__(self):
        self.dalex = importr('DALEX')
        self.model_down_package = importr('modelDown')
        self.predict_function_generator = PredictFunctionGenerator()
        # For conversion between R and NumPy objects
        numpy2ri.activate()

    def explain(self, model, data, labels, names):
        predict_function = self.predict_function_generator.generate_function(model)
        r_model = robjects.ListVector({'label': 'Keras Sequential'})
        r_data = robjects.DataFrame({names[x]:  robjects.FloatVector(data[:,x]) for x in range(data.shape[1])})
        return self.dalex.explain(model=r_model, data=r_data, y=labels, predict_function=predict_function)
    
    def generate_website(self, explainer):
        self.model_down_package.modelDown(explainer)