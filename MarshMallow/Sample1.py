from datetime import date
from pprint import pprint

from marshmallow import Schema, fields


class ArtistSchema(Schema):
    name = fields.Str()


class AlbumSchema(Schema):
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())


name = dict(name="ABC DEF")
album = dict(artist=name, title="Title", release_date=date(2022, 4, 5))

schema = AlbumSchema()
result = schema.dump(album)
pprint(result, indent=2)



