from django.conf.urls import include, url
from synonyms import views
urlpatterns = [
        url(r'^home/$',views.get_home, name="get_home"),
        url(r'^$',views.get_home, name="get_home"),
        url(r'^get_words/$', views.get_synonyms, name="get_synonyms")
        ]
