from rest_framework import serializers
from .models import Contestant

class ContestantSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True, required=False)

  class Meta:
    model = Contestant
    fields = ['id', 'name', 'email', 'phone', 'password', 'is_verified', 'created_at']

  def create(self, validated_data):
    password = validated_data.pop('password', None)
    user = Contestant.objects.create(**validated_data)
    if password:
      user.set_password(password)
      user.save()
    return user