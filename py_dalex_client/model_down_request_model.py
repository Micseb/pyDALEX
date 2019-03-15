class ModelDownRequestModel:
    def __init__(self, modules = None, output_folder = None, repository_name = None, remote_repository_path = None, device = None, vr_vars = None, vr_type = None):
        self.modules = modules
        self.output_folder = output_folder
        self.repository_name = repository_name
        self.remote_repository_path = remote_repository_path
        self.device = device
        self.vr_vars = vr_vars
        self.vr_type = vr_type