from marshmallow import Schema, fields, post_load, ValidationError, validates, validate


class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return f'{self.name} is {self.age} years old.'


class PersonSchema(Schema):
    name = fields.Str(validate=validate.Length(max =5))
    age = fields.Int()
    email = fields.Email()
    location = fields.Str(required=False)

    @validates('age')
    def validate_age(self, age):
        if age < 20:
            raise ValidationError('The age is too young!')
        elif age > 120:
            raise ValidationError('The age is too old!')

    # location = fields.Str(required=True)

    @post_load()
    def create_person(self, data, **kwargs):
        return Person(**data)


input_data = {}
input_data['name'] = input("Enter your name : ")
input_data['age'] = input("Enter Age: ")
input_data['email'] = input("Enter Email: ")

try:
    schema = PersonSchema()
    person = schema.load(input_data)
    result = schema.dump(person)
    print(result)
except ValidationError as err:
    print(err.messages)
