from django.urls import path,include
from . import views
from . import views as user_views
from django.contrib.auth import views as auth_views
from .views import TableCreateView,UserTableListView,TableDetailView,TableUpdateView,TableDeleteView


urlpatterns = [
    path('',views.home,name='home'),
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='table/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='table/logout.html'),name='logout'),
    path('table/new/',TableCreateView.as_view(),name='table-create'),
    path('user/<str:username>',UserTableListView.as_view(),name ='user-table'),
    path('table/<int:pk>/',TableDetailView.as_view(), name='table-detail'),
    path('table/<int:pk>/update/',TableUpdateView.as_view(),name='table-update'),
    path('table/<int:pk>/delete/',TableDeleteView.as_view(),name='table-delete'),

]
