from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home),
    url(r'clicked/',views.out),
#    url(r'customerreg/',views.insertcust),
    url(r'reg/',views.reg),
    url(r'regsub/',views.regsub),
    url(r'review/',views.review),
    url(r'reviewsub/',views.reviewsub),
    url(r'channel/',views.channel),
    url(r'channelsub/',views.channelsub),

]
