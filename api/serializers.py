from rest_framework import serializers
from .models import User, Category, Product

# User serializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    photo = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ['id', 'full_name', 'mobile_no', 'email', 'role', 'password', 'photo']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

# Category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']

# Product serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'details', 'price', 'image', 'category', 'seller', 'created_at', 'updated_at']