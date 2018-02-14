from django.conf.urls import url
from secund_app import views

urlpatterns = [
    url(r'^$', index.views, name='index')
]