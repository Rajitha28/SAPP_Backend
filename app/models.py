from mongoengine import Document, StringField

class Item(Document):
    name = StringField(required=True)
    description = StringField()
