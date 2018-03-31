from rest_framework import serializers
from webapp.models import *

class SnippetSerializer(serializers.ModelSerializer):
	class Meta:
		model=todo
		fields=('__all__')
