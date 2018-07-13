from django.urls import include,path,re_path
from . import views

app_name = 'reviews'

urlpatterns = [
    re_path(r'^$',views.review_list,name = 'review_list'),
    re_path(r'^review/(?P<review_id>[0-9]+)/$',views.review_detail,name = 'review_detail'),
    re_path(r'^wine$', views.wine_list, name='wine_list'),
    re_path(r'^wine/(?P<wine_id>[0-9]+)/$', views.wine_detail, name='wine_detail'),
    re_path(r'^wine/(?P<wine_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
]