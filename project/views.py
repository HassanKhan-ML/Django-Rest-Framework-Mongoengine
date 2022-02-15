from django.shortcuts import render
from rest_framework import viewsets
from .models import Page ,Tool
from .serializers import PageSerializer ,ToolSerializer ,PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework_mongoengine import viewsets

class ToolViewSet(viewsets.ModelViewSet):
  serializer_class = ToolSerializer

  def get_queryset(self):
    return Tool.objects.all()
      
# Create your views here.

@api_view(['GET'])
def getPage(request):

  notes = Page.objects.all().order_by('-updated')
  serializer = PageSerializer(notes,many=True)
  # authentication_classes = [TokenAuthentication, ]
  # permission_classes = [IsAuthenticated, ]
  return Response(serializer.data,)

# class PageViewSet(viewsets.ModelViewSet):
#   queryset = Page.objects.all()
#   serializer_class = PageSerializer
#   # queryset = Page.objects.all().order_by('-updated')
#   # authentication_classes = [TokenAuthentication, ]
#   # permission_classes = [IsAuthenticated, ]


from rest_framework_mongoengine.generics import *    
from rest_framework import filters    

@api_view(['GET'])
def ClientList(request):
    # serializer_class = PostSerializer
    queryset = Page.objects.all()
    serializer = PostSerializer(queryset,many=True)

    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields = ('name',)
    return Response(serializer.data,)