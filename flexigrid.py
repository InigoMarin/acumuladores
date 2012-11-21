import json

class JSONWrapper():
    def __init__(self, data):
        self.page = 0
        self.total = len(data)
        self.rows = data
