from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'^posts/(?P<post_id>\d+)/comments', views.CommentViewSet, basename='comments')

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('', include(router.urls)),
]
