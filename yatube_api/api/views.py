from rest_framework import viewsets

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

    def get_post_id(self):
        post_id = self.kwargs.get('post_id')
        return post_id

    def perform_create(self, serializer):
        post_id = self.get_post_id()
        serializer.save(author=self.request.user, post_id=post_id)

    def get_queryset(self):
        post_id = self.get_post_id()
        post = Post.objects.get(id=post_id)
        post = post.post_comments.all()
        if post is not None:
            queryset = post
        return queryset


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
