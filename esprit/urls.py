from  django.urls import  path
from  . import  views
urlpatterns=[
    path('',views.helloDjango, name='helloDjango'),
    path('index/<int:id>',views.detail,name='detail'),
    path('getAll/', views.getAll, name='getAll')
]