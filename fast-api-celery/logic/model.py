class FakeModel:
    def __init__(self):
        self.m = 7.0
        self.q = 0.5
    def predict(self, x):
        return self.m * x + self.q