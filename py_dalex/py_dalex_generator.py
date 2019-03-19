from .py_dalex import PyDalex
from .explain_model_mapper import ExplainModelMapper
from .model_down_model_mapper import ModelDownModelMapper

class PyDalexGenerator:   
    def generate_website(self, explain_request, model_down_request):
        explain_mapper = ExplainModelMapper()
        model_down_mapper = ModelDownModelMapper()
        explain_models = [explain_mapper.map(item) for item in explain_request]
        model_down_model = model_down_mapper.map(model_down_request, explain_request[0].column_names)

        # Dalex operations
        py_dalex = PyDalex()
        explainers = py_dalex.generate_explainers(explain_models)
        website_link = py_dalex.generate_website(explainers, model_down_model)
        return website_link