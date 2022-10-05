from django.urls import path, include
from .views import (
    home,
    FirmList,
    FirmDetail,
   
)

# from rest_framework import routers
# router=routers.DefaultRouter()
# router.register('firm',FirmGRUD)


urlpatterns = [
    path('', home),
#     path('student/', student_api),
#     path('student/<int:pk>/', student_api_get_update_delete, name="detail"),
#     path('path/', path_api),
    path('list/', FirmList.as_view(), name='FirmList'),
#     path('student_create/', student_create, name='student_create'),
    path('detail/<int:pk>/', FirmDetail.as_view(), name='FirmDetail'),
#     path('student_update/<int:pk>/', student_update, name='student_update'),
#     path('student_update_partial/<int:pk>/',
#          student_update_partial, name='student_update_partial'),
#     path('student_delete/<int:pk>/', student_delete, name='student_delete'),    
   
]