from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('posts', views.PostViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('', include(router.urls)),
    path('groups/', views.api_groups),
    path('groups/<int:group_id>/', views.api_group_detail),
    path('posts/<int:post_id>/comments/', views.api_comments),
    path(
        'posts/<int:post_id>/comments/<int:comment_id>/',
        views.api_comment_detail
    ),
]
