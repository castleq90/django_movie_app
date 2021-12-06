from django.urls import path
from movies import views

urlpatterns =[
    path('list/', views.MovieList.as_view()),
    path('detail/<int:pk>/',views.MovieDetail.as_view()),
]
