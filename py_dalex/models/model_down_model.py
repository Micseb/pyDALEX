class ModelDownModel:
    def __init__(self, modules, output_folder, repository_name, remote_repository_path, device, vr_vars, vr_type):
        self.modules = modules
        self.output_folder = output_folder
        self.repository_name = repository_name
        self.remote_repository_path = remote_repository_path
        self.device = device
        self.vr_vars = vr_vars
        self.vr_type = vr_type