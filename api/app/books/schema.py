from app.books.models import Book
from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields
from app import db


class BookSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Book
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    year = fields.Integer(required=True)
    author_id = fields.Integer()
