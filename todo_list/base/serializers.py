from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ToDo, File
import base64

class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = File
    fields = ('id', 'file', 'remark', 'timestamp')



class ToDoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ToDo
        fields = ['id', 'title', 'body', 'owner']


class UserSerializer(serializers.ModelSerializer):
    todo = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'todo']
