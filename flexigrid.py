import json

class JSONWrapper():
    def __init__(self, data):
        self.page = 0
        self.total = len(data)
        self.rows = data

    def convert(self):
        data = {"page": self.page, "total": self.total, "rows": json.dumps(self.rows)}
        return data
