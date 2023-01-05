
from django.contrib import admin
from django.urls import path
from registration1 import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', views.HomePage, name="home"),
    path('login/', views.LoginPage, name="login"),
    path('signup/', views.SignupPage, name="signup"),
    path('logout/', views.LogOut, name="logout"),
    path('wrong/', views.Wrong, name="wrong"),
    path('main/', views.Main, name="main"),
    # path('main/add-new-post', views.add_new_post, name="add-new-post"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
