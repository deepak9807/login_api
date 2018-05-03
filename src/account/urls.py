from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from account.views import (login_view,logout_view,register_view)
app_name = 'account'

urlpatterns = [

    url(r'^register/', register_view, name="register"),
    url(r'^login/', login_view, name="login"),
    url(r'^logout/', logout_view, name="logout"),
]