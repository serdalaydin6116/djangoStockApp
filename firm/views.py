from django.shortcuts import render,HttpResponse
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


def home(request):
    return HttpResponse('<h1>API Page</h1>')

class FirmList(APIView):
    #request.method==get
    def get(self,request):
        firms=Firm.objects.all()
        #due to there are more than one, we must use many=true
        serializer=FirmSerializer(firms, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=FirmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class FirmDetail(APIView):
    def get_obj(self,pk):
        return get_object_or_404(Student,pk=pk)
    
    def get(self,request,pk):
        firm=self.get_obj(pk)
        serializer=FirmSerializer(firm)
        return Response(serializer.data)
    
    def put(self,request,pk):
        firm=self.get_obj(pk)
        serializer=FirmSerializer(firm,data=request.data)
        if serializer.is_valid():
            serializer.save()
            new_data=serializer.data
            new_data['success']=f"Firm {firm.f_name} updated successfuly"
            return Response(new_data)    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
    
    def delete(self,request,pk):
        firm=self.get_obj(pk)
        firm.delete()
        data={
            "message":f"Firm {firm.f_name} deleted successfuly"
        }
        return Response(data,status=status.HTTP_204_NO_CONTENT)

### CBV ### ### Generic APIView ###
# class FirmListCreate(mixins.ListModelMixin,mixins.CreateModelMixin,GenericAPIView):
#     queryset=Firm.objects.all()
#     serializer_class=FirmSerializer
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

# class FirmURD(mixins.UpdateModelMixin,
#                 mixins.RetrieveModelMixin,
#                 mixins.DestroyModelMixin,
#                 GenericAPIView
#             ):   
#     queryset=Firm.objects.all()
#     serializer_class=FirmSerializer
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)

#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)

#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)

### CBV ### ### Concrate APIView ###
# class FirmLC(ListCreateAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

# class FirmRUD(RetrieveUpdateDestroyAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer



























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



