from rest_framework import serializers
from news.models import Posts, Comments, Like, User


class PostsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    body = serializers.CharField()
    created = serializers.DateTimeField()


class LikesSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        like = Like.objects.create(**validated_data)
        return like

    class Meta:
        model = Like
        fields = ['post', 'author', 'like']


class CommentsSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        comment = Comments.objects.create(**validated_data)
        return comment

    class Meta:
        model = Comments
        fields = ['post', 'author', 'body', 'created']


class PostSerializer(serializers.ModelSerializer):
    # comments_post = CommentsSerializer(many=True, read_only=True)
    # likes = LikesSerializer(many=True, read_only=True)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.body = validated_data.get('body', instance.body)
    #     instance.image = validated_data.get('image', instance.image)
    #     instance.alt_image = validated_data.get('alt_image', instance.alt_image)
    #     instance.likes = validated_data.get('likes', instance.likes)
    #     instance.comments_post = validated_data.get('comments_post', instance.comments_post)

        # instance.email = validated_data.get('email', instance.email)

        # instance.save()
        # return instance
    
    class Meta:
        model = Posts
        fields = ['title', 'body', 'image', 'comments_post', 'likes']

    

class ProfileSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        # instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class CatSerializer(serializers.Serializer):
    category_names = serializers.CharField(max_length=150)