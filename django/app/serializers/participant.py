from rest_framework import serializers

from app.serializers.hobby import Hobby


class Participant(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    age = serializers.IntegerField()
    hobbies = Hobby(many=True)
