from .models.model_down_model import ModelDownModel
import rpy2.rinterface as rinterface
import uuid
import os.path

class ModelDownModelMapper:
    def map(self, request_model, column_names):
        website_id = str(uuid.uuid4())
        modules = request_model.modules or ["auditor", "drifter", "model_performance", "variable_importance", "variable_response"]
        output_folder = os.path.join(request_model.output_folder or "output", website_id)
        repository_name = request_model.repository_name or "repository"
        remote_repository_path = request_model.remote_repository_path or rinterface.NULL
        device = request_model.device or "png"
        vr_vars = request_model.vr_vars or column_names
        vr_type = request_model.vr_type or "pdp"
        return ModelDownModel(modules, output_folder, repository_name, remote_repository_path, device, vr_vars, vr_type)