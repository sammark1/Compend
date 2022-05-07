from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('user/<username>/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('campaign/', views.Campaign_List.as_view(), name="Campaign_List"),
    path('campaign/create/', views.Campaign_Create.as_view(), name="Campaign_Create"),
    path('campaign/<int:campaign_id>', views.Campaign_Show, name="Campaign_Show"),

]