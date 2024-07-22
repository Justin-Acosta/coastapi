from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from coastapi.models import *
from coastapi.views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'players', Players, 'player')
router.register(r'shop', Shop, 'shop')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

