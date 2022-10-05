from django.shortcuts import render
from.models import Firm, Brand, Category, Stock, Product
from .serializers import FirmSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView 
from rest_framework.generics import GenericAPIView,mixins,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action


from .pagination import SmallPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class productCRUD(ModelViewSet):
    queryset=Product.objects.all().order_by('-id')
    serializer_class=FirmSerializer
    pagination_class= SmallPageNumberPagination
    

    ## add filterset fields
    filter_backends=[DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields=['f_name', 'phone']
    filterset_fields=['first_name', 'last_name', 'number']
    ordering_fields=['id', 'first_name', 'last_name']
    
    
    def get_queryset(self):
        queryset=Student.objects.all()
        path = self.request.query_params.get('path')
        if path is not None:
            mypath = Path.objects.get(path_name=path)
            queryset = queryset.filter(path=mypath.id)
        return queryset


    @action(detail=False,methods=['GET'])
    def student_count(self,request):
        count={
            'student-count':self.queryset.count()
        }
        return Response(count)



