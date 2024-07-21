from rest_framework import serializers
from .models import Task, Comment, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField()
    tags = TagSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['name', 'description', 'due_date', 'status', 'comments_count', 'comments', 'tags']

    def get_comments_count(self, obj) -> int:
        return obj.comments.count()



