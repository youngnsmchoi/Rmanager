"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inventory import views
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('reagent/', views.reagent, name='reagent'),
    path('reagentcreate/', views.reagentcreate, name='reagentcreate'),
    path('detail/<int:management_id>', views.detail, name='detail'),
    path('management_modify/<int:management_id>/', views.management_modify, name="management_modify"),
    path('management_delete/<int:management_id>/', views.management_delete, name='management_delete'),

    path('consumables/', views.consumables, name="consumables"),
    path('consumablecreate/', views.consumablecreate, name='consumablecreate'),
    path('con_detail/<int:question_id>', views.con_detail, name='con_detail'),
    path('question_modify/<int:question_id>/', views.question_modify, name="question_modify"),
    path('question_delete/<int:question_id>/', views.question_delete, name='question_delete'),

    path('control/', views.control, name='control'),
    path('controlcreate/', views.controlcreate, name='controlcreate'),
    path('trol_detail/<int:takeout_id>', views.trol_detail, name='trol_detail'),
    path('takeout_modify/<int:takeout_id>/', views.takeout_modify, name="takeout_modify"),
    path('takeout_delete/<int:takeout_id>/', views.takeout_delete, name='takeout_delete'),

    path('login/', accounts_views.login, name="login"),
    path('logout/', accounts_views.logout, name="logout"),

    path('signup/',accounts_views.signup, name="signup"),

    path('accounts/', include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)