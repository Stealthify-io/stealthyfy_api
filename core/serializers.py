
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from core.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(min_length=8)
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
        

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
