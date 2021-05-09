from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload, name='upload'),
    path('details/<str:number>', views.book_details, name='book_details'),
    path('modify/<str:number>', views.modify, name='modify'),
    path('delete/<str:number>', views.delete, name='delete'),
    path('upload_history', views.list_history, name='upload_history'),
]