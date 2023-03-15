from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
# from store.models import Customer
# from rest_framework import serializers

class UserCreateSerializer(BaseUserCreateSerializer):
  # birth_date = serializers.DAteField()
  
  class Meta(BaseUserCreateSerializer.Meta):
    fields = ['id',
              'username',
              'email',
              'password',
              'first_name',
              'last_name'
              # 'birth_date'
    ]


class UserSerializer(BaseUserSerializer):
  class Meta(BaseUserSerializer.Meta):
    fields = ['id',
              'username',
              'email', 'first_name', 'last_name']