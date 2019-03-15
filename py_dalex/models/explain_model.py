class ExplainModel:
    def __init__(self, model, data, y, predict_function, label, link):
        self.model = model
        self.data = data
        self.y = y
        self.predict_function = predict_function
        self.label = label
        self.link = link