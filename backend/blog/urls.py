from django.urls import include, path
from . import views



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('list/', views.PostList.as_view()),
    path('details/<slug:slug>/', views.PostDetail.as_view()),
]