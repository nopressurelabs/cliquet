import colander

from cliquet.resource import Resource, Schema, crud

class MushroomSchema(Schema):
    name = colander.SchemaNode(colander.String())


@crud()
class Mushroom(Resource):
    mapping = MushroomSchema()
