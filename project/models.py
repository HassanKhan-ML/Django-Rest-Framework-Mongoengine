from django.db import models
# from mongoengine import Document, EmbeddedDocument, fields
# Create your models here.

# from mongoengine import Document ,fields
# from mongoengine import *
from mongoengine import Document, EmbeddedDocument, fields , DynamicDocument , StringField

# class Blogs(Document):
#   name = fields.StringField()
#   topic = fields.StringField()
#   date = fields.DateTimeField()
#   addition_info = fields.DictField()

class Tool(Document):
	label = fields.StringField(required=True)
	description = fields.StringField(required=True, null=True)

class Page(DynamicDocument):
	title = StringField(max_length=200, required=True)




class User(Document):
	email = StringField(required=True)
	first_name = StringField(max_length=50)
	last_name = StringField(max_length=50)

# class BlogPost(Document):
#     # author = fields.StringField(verbose_name="Name", max_length=255)
#     # email  = fields.EmailField(verbose_name="Email")
#     # body = fields.StringField(verbose_name="Comment")
#     title = StringField(required=True, max_length=200)
#     tags = ListField(StringField(max_length=50))
    # meta = {'allow_inheritance': True}

# class TextPost(BlogPost):
#     content = StringField(required=True)

# class LinkPost(BlogPost):
#     url = StringField(required=True)