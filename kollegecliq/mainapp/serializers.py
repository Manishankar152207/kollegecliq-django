from rest_framework import serializers
from traitlets import default
from mainapp.models import RegisteredUsers,Contact,RegisteredCollege
import uuid
class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=55,required=True)
    name = serializers.CharField(max_length=55,required=True)
    email = serializers.EmailField(required=False)
    phone = serializers.CharField(max_length=14, required=False)
    password = serializers.CharField(max_length=260, required=False)

    class Meta:
        model = RegisteredUsers 
        fields = ['username','name','email','phone','password']

class CollegeRegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=55,required=True)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(max_length=14, required=True)
    state = serializers.CharField(max_length=55, required=True)
    city = serializers.CharField(max_length=55, required=True)
    area = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=260, required=True)

    class Meta:
        model = RegisteredCollege 
        fields = ['name','email','phone','state','city','area','password']


class ContactSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    message = serializers.CharField(required=True)

    class Meta:
        model = Contact 
        fields = ['name','email','message']
