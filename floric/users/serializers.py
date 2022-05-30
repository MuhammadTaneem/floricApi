from rest_framework import serializers
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# User = get_user_model()

from .models import User
# from django.contrib.auth import get_user_model
# # User = get_user_model()
from djoser.serializers import UserCreateSerializer

# from .models import User

class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = '__all__'

    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


# from .models import User


# class UserDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['date_joined',
#                   "first_name",
#                   "last_name",
#                   "email",
#                   "image",
#                   "phone",
#                   "date_of_birth",
#                   "gender",
#                   "date_of_birth",
#                   "city",
#                   "address"]


# from rest_framework import serializers
# from .models import User
# from django.contrib.auth import get_user_model
# # User = get_user_model()
# from djoser.serializers import UserCreateSerializer
#
#
# class UserSerializer(UserCreateSerializer):
#     class Meta(UserCreateSerializer.Meta):
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'password']