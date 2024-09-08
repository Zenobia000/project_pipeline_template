# Pipeline Step Base Class
class Step:
    def __init__(self, name):
        self.name = name

    def execute(self, data):
        raise NotImplementedError("Execute method must be overridden by subclasses")