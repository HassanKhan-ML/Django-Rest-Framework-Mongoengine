
from rest_framework.serializers import ModelSerializer
from rest_framework_mongoengine import serializers

from .models import Page ,Tool

class PageSerializer(ModelSerializer):
	class Meta:
		model = Page
		fields = '__all__'


class ToolSerializer(serializers.DocumentSerializer):
	class Meta:
		model = Tool
		fields = '__all__'


from rest_framework_mongoengine.serializers import DocumentSerializer

class PostSerializer(DocumentSerializer):
	class Meta:
		# model = Tool
		model = Page

		depth = 2




