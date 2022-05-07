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
    path('campaign/<int:pk>', views.Campaign_Show.as_view(), name="Campaign_Show"),
    path('campaign/<int:pk>/update', views.Campaign_Update.as_view(), name="Campaign_Update"),
    path('campaign/<int:pk>/delete', views.Campaign_Delete.as_view(), name="Campaign_Delete"),
    path('npc/', views.NPC, name="NPC"),
    path('npc/create/', views.NPC_Create.as_view(), name="NPC_Create"),
    path('npc/<int:pk>', views.NPC_Show.as_view(), name="NPC_Show"),
    path('npc/<int:pk>/update', views.NPC_Update.as_view(), name="NPC_Update"),
    path('npc/<int:pk>/delete', views.NPC_Delete.as_view(), name="NPC_Delete"),
]