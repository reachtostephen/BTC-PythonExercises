import json


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "%s %s" % (self.first_name, self.last_name)

    @classmethod
    def getAll(self):
        result = []
        with open('db.json') as j:
            json_list = json.load(j)
        for item in json_list['names']:
            person = Person(item['first_name'], item['last_name'])
            result.append(person)
        return result
