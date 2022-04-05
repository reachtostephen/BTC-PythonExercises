import datetime as dt
import uuid

from marshmallow import Schema, fields, post_load, ValidationError, validate, validates, INCLUDE
from pprint import pprint
from collections import OrderedDict  # Preseves order in which inserted

'''
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return "<User(name={self.name!r})>".format(self=self)
'''

# Schema Creation
'''
class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
'''

'''
# Alternative
UserSchema = Schema.from_dict(
    {"name": fields.Str(), "email": fields.Email(), "created_at": fields.DateTime()}
)

# Serializing
user = User(name="ABC", email="abc@gmail.com")
schema = UserSchema()
result = schema.dump(user)
pprint(result)

# JSON
json_result = schema.dumps(user)  # dumps - json
pprint(json_result)

# Filtered Output
filtered_schema = UserSchema(only=("name", "email"))
print(filtered_schema.dump(user))

# DeSerializing
user_data = {
    "created_at": "2022-04-05T11:52:44.415032",
    "email": "abc@gmail.com",
    "name": "ABC"
}

schema = UserSchema()
result = schema.load(user_data)
pprint(result)


user_data = {"name": "abc", "email": "ABC@gmail.com"}
schema = UserSchema()
result = schema.load(user_data)
print(result) #Now print can display the schema object

# Serializing collection of objects
user1 = User(name="Mick", email="mick@stones.com")
user2 = User(name="Keith", email="keith@stones.com")
users = [user1, user2]
schema = UserSchema(many=True)
result = schema.dump(users)  # OR UserSchema().dump(users, many=True)
pprint(result)
'''

# Validation
'''
try:
    result = UserSchema().load({"name": "ABC", "email": "abc"})  # Not a valid email address
except ValidationError as err:
    print(err.messages)  # Prints all the error messages
    print(err.valid_data)  # Prints the valid data


class BandMemberSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email()


user_data = [
    {"name": "ABC", "email": "abc@gmail.com"},
    {"name": "DEF", "email": "def"},  # Wrong email
    {"name": "GHI", "email": "ghi@gmail.com"},
    {"email": "jkl@gmail.com"},  # Missing name
]

try:
    BandMemberSchema(many=True).load(user_data)
except ValidationError as err:
    pprint(err.messages)
'''

'''
def validate_quantity(n):
    if n < 0:
        raise ValidationError("Quantity is not acceptable (Must be greater than 0)")
    elif n > 30:
        raise ValidationError("Quantity is not acceptable (Must be max 30)")


class UserSchema(Schema):
    name = fields.Str(validate=validate.Length(min=1))
    permission = fields.Str(validate=validate.OneOf(["read", "write", "admin"]))
    age = fields.Int(validate=validate.Range(min=18, max=40))


class ItemSchema(Schema):
    quantity = fields.Integer()

    @validates('quantity')
    def validate_quantity(self, value):
        if value < 0:
            raise ValidationError("Quantity is not acceptable (Must be greater than 0)")
        elif value > 30:
            raise ValidationError("Quantity is not acceptable (Must be max 30)")


# data = {"name": "", "permission": "other", "age": 16}
# try:
#     UserSchema().load(data)
# except ValidationError as err:
#     print(err.messages)

data = [{'quantity': -1},
        {'quantity': 31}]

try:
    result = ItemSchema().load(data, many=True)
except ValidationError as err:
    print(err.messages)
'''

'''
# Required Fields
class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True, error_messages={"required": "Age is required."})
    city = fields.String(
        required=True,
        error_messages={"required": {"message": "City required", "code": 400}},
    )
    email = fields.Email()
'''

'''
try:
    result = UserSchema().load({"email": "foo@bar.com"})
except ValidationError as err:
    pprint(err.messages)
'''

# To skip this Validation use Partial

# result = UserSchema().load({'age': 21}, partial=True)  # No error displayed
# print(result)

'''
class UserSchema(Schema):
    class Meta:
        unknown = INCLUDE

    id = fields.UUID(load_only=True, load_default=uuid.uuid1)
    birthdate = fields.DateTime(dump_only=True, dump_default=dt.datetime(2022, 4, 5))


pprint(UserSchema().load({'age': 21}, unknown=INCLUDE))
print(UserSchema().dump({}))
'''

'''
class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True, error_messages={"required": "Age is required."})
    city = fields.String(
        required=True,
        error_messages={"required": {"message": "City required", "code": 400}},
    )
    email = fields.Email()


errors = UserSchema().validate({"name": "ABC", "email": "abc"})  # Validates without load creating an object
print(errors)
'''

# data_key
'''
class UserSchema(Schema):
    name = fields.String()
    email = fields.Email(data_key='emailAddress')


data = {'name': 'ABC', 'email': 'abc@gmail.com'}

print(UserSchema().dump(data))

data = {'name': 'ABC', 'emailAddress': 'abc@gmail.com'}
print(UserSchema().load(data))
'''


class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return "<User(name={self.name!r})>".format(self=self)


class UserSchema(Schema):
    first_name = fields.String()
    last_name = fields.String()
    email = fields.Email()

    class Meta:
        ordered = True


u = User("Abc", "Def", "abc@gmail.com")
schema = UserSchema()
result = schema.dump(u)

assert isinstance(result, OrderedDict)
pprint(result, indent=2)
