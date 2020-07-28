from .models import User_Emp
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Emp
        fields = ['id','email', 'first_name', 'last_name']#, 'avatar']