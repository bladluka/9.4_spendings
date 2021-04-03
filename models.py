import json

class Spendings:
    def __init__(self):
        try:
            with open("spendings.json", "r") as f:
                self.spendings = json.load(f)
        except FileNotFoundError:
            self.spendings = []

    def all(self):
        return self.spendings

    def get(self, id):
        return self.spendings[id]

    def create(self, data):
        data.pop('csrf_token')
        self.spendings.append(data)

    def update(self, id, data):
        data.pop('csrf_token')
        self.spendings[id] = data

    def save_all(self):
        with open("spendings.json", "w") as f:
            json.dump(self.spendings, f)

    def delete(self, id):
        spending = spendings.get(id)
        self.spendings.remove(spending)

spendings = Spendings()