from django.contrib import admin
from django.urls import path

from api import views
from myapp1.views import index_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('api/<str:s>', views.StatisticsView.as_view())
]
