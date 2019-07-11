from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import SimpleRouter

from meiduo_admin.views.login_views import LoginView
from meiduo_admin.views.home_views import *
from meiduo_admin.views.user_manage_views import *

urlpatterns = [
    # url(r'^authorizations/$', LoginView.as_view()),

    url(r'^authorizations/$', obtain_jwt_token),

    url(r'^users/$', UserView.as_view())

]

router = SimpleRouter()
router.register(prefix='statistical', viewset=HomeViewSet, base_name='home')

urlpatterns += router.urls