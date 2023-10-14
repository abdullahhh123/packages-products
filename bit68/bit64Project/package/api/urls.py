from django.urls import path
from . import views

urlpatterns = [
    path('packages',views.packages),
    path('packages/<str:pk>/',views.get_package_by_name),
    path('package/post',views.package_post),
    # SUBSCRIPTION
     path('make-order',views.subscription_post),
    # path('Create-playlist/',views.CreateVideosPerPlayList),
]