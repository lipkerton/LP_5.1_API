from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from posts.models import Group, Post
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

    def get_post(self):
        return (get_object_or_404(Post, id=self.kwargs.get('post_id')))

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post = self.get_post()
        return post.post_comments.all()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
