from pprint import pprint
import inspect


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introspection_info(self):
        return f'Hello! My name is {self.name}, I am {self.age} years old.'


person = Person('Maria', 35)
# print(person.introspection_info())

info = {'type': type(person).__name__, 'attributes': [], 'methods': []}

for attr in dir(person):
    if callable(getattr(person, attr)):
        info['methods'].append(attr)
    else:
        info['attributes'].append(attr)

    module = inspect.getmodule(person)
    if module is None:
        info['module'] = __name__
    else:
        info['module'] = module.__name__

pprint(info)
