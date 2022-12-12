from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from posts.models import Group, Post
from api.serializers import CommentSerializer, PostSerializer, GroupSerializer,FollowSerializer
from api.permissions import IsAuthorReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsAuthorReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username','user__username')

    def get_queryset(self):
        return self.request.user.follower

    def perfom_create(self, serializer):
        serializer.save(user=self.request.user)



class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        post_obj = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post_obj.comments.all()

    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsAuthorReadOnly)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(
            author=self.request.user,
            post=post)
