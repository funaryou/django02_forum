from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("register/",views.register,name="register"),
    path("login/",auth_views.LoginView.as_view(template_name="login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(next_page='login'),name="logout"),
    path('profile/edit/<int:pk>', views.profile_edit, name='profile_edit'),
    path('profile/detail/<int:pk>', views.profile_detail, name='profile_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)