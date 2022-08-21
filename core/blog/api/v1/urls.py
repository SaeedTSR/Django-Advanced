from django.urls import path
from . import views

urlpatterns = [
    path('post',view=views.list_api_view,name='list-api'),
    path('post/<int:id>',view=views.detail_api_view,name='detail-api')
]
