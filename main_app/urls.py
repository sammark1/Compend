from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('user/<username>/', views.profile, name='profile'),
    path('user/<int:pk>/update', views.profile_update.as_view(), name='profile_update'),
    path('user/<username>/delete', views.profile_delete, name='profile_delete'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('campaign/', views.Campaign_List.as_view(), name="Campaign_List"),
    path('campaign/create/', views.Campaign_Create.as_view(), name="Campaign_Create"),
    path('campaign/<int:pk>', views.Campaign_Show.as_view(), name="Campaign_Show"),
    path('campaign/<int:pk>/update', views.Campaign_Update.as_view(), name="Campaign_Update"),
    path('campaign/<int:pk>/delete', views.Campaign_Delete.as_view(), name="Campaign_Delete"),
    path('campaign/<int:pk>/npc/', views.NPC_List.as_view(), name="NPC_List"),
    path('campaign/<int:pk>/npc/create/', views.NPC_Create.as_view(), name="NPC_Create"),
    path('npc/<int:pk>', views.NPC_Show.as_view(), name="NPC_Show"),
    path('npc/<int:pk>/update', views.NPC_Update.as_view(), name="NPC_Update"),
    path('npc/<int:pk>/delete', views.NPC_Delete.as_view(), name="NPC_Delete"),
    path('location/', views.Location_List.as_view(), name="Location_List"),
    path('location/create/', views.Location_Create.as_view(), name="Location_Create"),
    path('location/<int:pk>', views.Location_Show.as_view(), name="Location_Show"),
    path('location/<int:pk>/update', views.Location_Update.as_view(), name="Location_Update"),
    path('location/<int:pk>/delete', views.Location_Delete.as_view(), name="Location_Delete"),
    path('upload/<int:pk>', views.upload_csv, name='upload_csv'),
]