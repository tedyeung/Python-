from django.conf.urls import url
from secund_app import views

urlpatterns = [
    urlr(r'^$', index.views, name='index')
]