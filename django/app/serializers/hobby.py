from rest_framework import serializers


class Hobby(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    since = serializers.DateField()
