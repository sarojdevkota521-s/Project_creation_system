from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'username','password', 'password1']

    def create(self, validated_data):
        # user = User.objects.create_user(
        #     email=validated_data['email'],
        #     username=validated_data['username'],
        #     password=validated_data['password']
        # )
        # return user
        
        if validated_data['password'] != validated_data['password1']:
            raise serializers.ValidationError("Passwords do not match.")
        return User.objects.create_user(**validated_data)