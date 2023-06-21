from django.urls import path
from . import views


urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('create/', views.student_create, name='student_create'),
    path('update/<int:student_id>/', views.student_update, name='student_update'),
    path('delete/<int:student_id>/', views.student_delete, name='student_delete'),
    path('book/', views.book_list, name='book_list'),
    path('createbook/', views.book_create, name='book_create'),
    path('updatebook/<int:pk>/', views.book_update, name='book_update'),
    path('deletebook/<int:pk>/', views.book_delete, name='book_delete'),
    path('studentspage/', views.student_page, name='student_page'),
    path('bookspage/', views.book_page, name='book_page'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
