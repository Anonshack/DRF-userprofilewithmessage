from django.urls import path, include
from rest_framework.routers import DefaultRouter
from social_network.users.views import UserViewSet, FriendshipViewSet
from django.contrib import admin

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'friendships', FriendshipViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
