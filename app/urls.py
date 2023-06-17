from django.urls import path,include
from .views import  CustomLoginView,RegisterPage,render_dashboard,upload_music
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/dashboard', render_dashboard, name='dashboard'),
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('dashboard', render_dashboard, name='dash'),
    path('upload/',upload_music, name='upload'),
]

