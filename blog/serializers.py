from rest_framework import serializers
from .models import Article , Category , UserProfile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class SelectArticleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True,allow_null=False,allow_blank=False,max_length=128)
    cover = serializers.CharField(required=True,allow_null=False,allow_blank=False,max_length=256)
    content = serializers.CharField(required=True,allow_null=False,allow_blank=False,max_length=2048)
    created_at = serializers.DateTimeField(required=True,allow_null=False)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['user']


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    author = UserProfileSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class AddArticleSerializer(serializers.ModelSerializer):
    author = serializers.CharField(max_length=128,allow_null=False,allow_blank=False)
    category = serializers.CharField(max_length=256,allow_blank=False,allow_null=False)

    class Meta:
        model = Article
        fields = '__all__'

    def validate_author(self,value):
        user = get_object_or_404(User,username=value)
        return UserProfile.objects.get(user=user)

    def validate_category(self,value):
        return get_object_or_404(Category,title=value)

    def create(self, validated_data):
        return Article.objects.create(**validated_data)


class UpdateArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('title','content')


    def update(self, instance, validated_data):
        instance.content = validated_data['content']
        instance.save()
        return instance

