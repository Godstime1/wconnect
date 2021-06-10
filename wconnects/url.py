from django.urls import path, include
from .import views

urlpatterns = [
    path('',views.home ),
    path('account/', views.account),
    path('signup/', views.signup),
    path('fb/', views.fb),
    path('ig/', views.ig),
    path('tw/', views.tw),

]