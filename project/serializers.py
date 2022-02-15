
from rest_framework_mongoengine import serializers

from .models import Page ,Tool

class PageSerializer(serializers.DocumentSerializer):
	class Meta:
		model = Page
		fields = '__all__'


class ToolSerializer(serializers.DocumentSerializer):
	class Meta:
		model = Tool
		fields = '__all__'




class PostSerializer(serializers.DocumentSerializer):
	class Meta:
		# model = Tool
		model = Page
		fields = '__all__'



