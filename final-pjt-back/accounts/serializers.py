from movies.serializers import GenreSerializer
from rest_framework import serializers

from .models import User


# 팔로우 등록 및 해제 : 팔로우 수까지
class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


# 싹다 넣음
class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    followings_count = serializers.SerializerMethodField()
    followers_list = FollowSerializer(many=True, read_only=True, source='followings')
    followings_list = FollowSerializer(many=True, read_only=True, source='followers')
    liked_genres = serializers.SerializerMethodField()

    def get_followers_count(self, obj):
        return obj.followings.count()

    def get_followings_count(self, obj):
        return obj.followers.count()

    def get_liked_genres(self, obj):
        genres = obj.liked_genres.all()
        return GenreSerializer(genres, many=True).data

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'sex', 'profile', 'followers_count', 'followings_count', 'followers_list', 'followings_list', 'liked_genres'
        )


class ExtendedUserSerializer(UserSerializer):
    followers = FollowSerializer(many=True, read_only=True)
    followings = FollowSerializer(many=True, read_only=True)

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('followers', 'followings')
