from django.conf.urls import url
from .views import MainView

urlpatterns = [
    url(r'^main/$', MainView.as_view(), name="main"),
]
