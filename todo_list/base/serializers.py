"""Документация."""
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ToDo, File


class FileSerializer(serializers.ModelSerializer):
    """Документация."""

    class Meta():
        """Документация."""

        model = File
        fields = ('id', 'file', 'remark', 'timestamp')


class ToDoSerializer(serializers.ModelSerializer):
    """Документация."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Документация."""

        model = ToDo
        fields = ['id', 'title', 'body', 'owner']


class UserSerializer(serializers.ModelSerializer):
    """Документация."""

    todo = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        """Документация."""

        model = User
        fields = ['id', 'username', 'todo']
