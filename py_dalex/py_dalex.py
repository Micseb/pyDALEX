import rpy2.robjects as robjects
import rpy2.robjects.numpy2ri as numpy2ri
from rpy2.robjects.packages import importr

class PyDalex:  
    def __init__(self):
        self._dalex_package = importr('DALEX')
        self._model_down_package = importr('modelDown')
        # For conversion between R and NumPy objects
        numpy2ri.activate()

    def generate_explainers(self, models):
        return [self.explain(model) for model in models]

    def explain(self, model):
        return self._dalex_package.explain(model = model.model, data = model.data, y = model.y, predict_function = model.predict_function, label = model.label)
    
    def generate_website(self, explainers, model):
        self._model_down_package.modelDown(*explainers, modules = model.modules, output_folder = model.output_folder, repository_name = model.repository_name, should_open_website=False, device = model.device, vr_type = model.vr_type, vr_vars = model.vr_vars, remote_repository_path = model.remote_repository_path)
        return model.output_folder