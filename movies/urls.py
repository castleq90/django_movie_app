from django.urls import path
from movies import views

urlpatterns =[
    path('list', views.MovieList.as_view()),
    # path('blog/<int:pk>/', views.BlogDetail.as_view()),
]
