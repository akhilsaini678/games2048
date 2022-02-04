from django.urls import path
from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name='index'),
    path("unicorn/", include("django_unicorn.urls")),
]