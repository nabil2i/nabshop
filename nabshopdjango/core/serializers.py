from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
  # def save(self, **kwargs):
  #   user = super().save(**kwargs)
  #   Customer.objects.create(user=user)

  class Meta(BaseUserCreateSerializer.Meta):
    fields = ['id',
              'username',
              'email',
              'password',
              'first_name',
              'last_name'
    ]
