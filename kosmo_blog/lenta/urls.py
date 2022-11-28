from django.urls import path
from . import views

urlpatterns = [
   path('', views.lenta_home, name='lenta_home'),
   path('create', views.create, name='create'),
   path('<int:pk>', views.new_detail_view.as_view(), name='new_detail'),
   path('<int:pk>/update', views.new_update_view.as_view(), name='new_update'),
   path('<int:pk>/delete', views.new_delete_view.as_view(), name='delete'),

]