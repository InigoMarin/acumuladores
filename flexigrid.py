import json

class JSONWrapper():
    def __init__(self, data):
        self.page = 1
        self.total = len(data)
        self.rows = data
