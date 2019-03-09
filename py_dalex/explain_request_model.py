class ExplainRequestModel:
    def __init__(self, model, data, y, column_names, predict_function = None, label = None, link = None):
        self.model = model
        self.data = data
        self.y = y
        self.column_names = column_names
        self.predict_function = predict_function
        self.label = label
        self.link = link