from rest_framework import serializers
from mainapp.models import RegisteredUsers

class RegisterSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(max_length=55, required=True)
    username = serializers.CharField(max_length=55,required=True)
    name = serializers.CharField(max_length=55,required=True)
    email = serializers.EmailField(required=False)
    phone = serializers.CharField(max_length=14, required=False)
    password = serializers.CharField(max_length=260, required=False)

    class Meta:
        model = RegisteredUsers 
        fields = ['user_id','username','name','email','phone','password']
