from django.urls import path
from .import views
urlpatterns = [
    path('',views.home, name="home"),
    path('insert_data',views.insert_data, name="insert_data"),
    path('login', views.login, name="login"),
    path('services',views.services, name="services"),
    path('next_page',views.next_page, name="next_page"),
    path('predict_data',views.predict_data, name='predict_data'),
    path('inside_loin',views.inside_loin,name='inside_loin'),
    path('contacting',views.contacting,name="contacting"),
    path('collected_data',views.collected_data,name='collected_data')
]

#    
#path('my_form/', views.my_view, name='my_view'),