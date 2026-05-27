from rest_framework import serializers
from .models import Interaction
from apps.users.serializers import UserSerializer


class InteractionSerializer(serializers.ModelSerializer):
    user_detail = UserSerializer(source='user', read_only=True)

    class Meta:
        model = Interaction
        fields = ('id', 'ticket', 'user', 'user_detail', 'message', 'created_at')
        read_only_fields = ('id', 'user', 'ticket', 'created_at')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)