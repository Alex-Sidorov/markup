from django.contrib.auth.models import User
from rest_framework import serializers
from guardian.shortcuts import assign_perm

from ..models.files import File


class FileSerializer(serializers.Serializer):

    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=128)
    text = serializers.CharField(allow_blank=True)
    author = serializers.ReadOnlyField(source='author.username')

    def create(self, validated_data):
        return File.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance


class FileMetaSerializer(serializers.Serializer):

    pk = serializers.IntegerField(read_only=True)
    title = title = serializers.CharField(required=True, max_length=128)