from rest_framework import viewsets

from posts.models import Comment, Group, Post
from .serializers import CommentSerializer, GroupSerializer, PostSerializer
from .permissions import IsAuthor


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthor,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthor,)

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        serializer.save(author=self.request.user, post_id=post_id)

    def get_queryset(self):
        queryset = Comment.objects.all()
        post_id = self.kwargs.get('post_id')
        if post_id is not None:
            queryset = queryset.filter(post_id=post_id)
        return queryset


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ['get']
