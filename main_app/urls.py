from django.urls import path
from . import views

urlpatterns = [ # always want PLURAL (unless in int:cat_id)
    path('', views.index, name='home'), # 'home' needs to match 'home' in DEF SIGNUP (views.py) 
    path('login/', views.login_view, name='login'), # '/login' needs to match BASE.html (path 'login/')
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name='signup'), # '/signup' needs to match BASE.html (path 'signup/')
    path('skills', views.skills_index, name='skills_index'),
    path('skills/<int:skill_id>', views.skills_detail, name='skills_detail'), #make sure detail isn't details
]