from django.urls import path

from main_diary import views

urlpatterns = [
    path('', views.DiaryList.as_view()),
    path('<int:pk>', views.DiaryDetail.as_view()),
    path('create_diary/', views.DiaryCreate.as_view()),
]
