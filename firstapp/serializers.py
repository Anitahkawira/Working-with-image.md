from .models import Todos
from rest_framework import serializers

class TodosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todos
        fields = ('userId', 'id', 'title', 'body', 'picture')
        