from django.shortcuts import render
from rest_framework import viewsets
from .models import Page ,Tool
from .serializers import PageSerializer ,ToolSerializer ,PostSerializer
from rest_framework.decorators import api_view 
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework_mongoengine import viewsets

from rest_framework import mixins,viewsets,generics


class ToolViewSet(viewsets.ModelViewSet):
  serializer_class = ToolSerializer

  def get_queryset(self):
    return Tool.objects.all()
      
# Create your views here.

# @api_view(['GET'])
# def getPage(request):

#   notes = Page.objects.all().order_by('-updated')
#   serializer = PageSerializer(notes,many=True)
#   # authentication_classes = [TokenAuthentication, ]
#   # permission_classes = [IsAuthenticated, ]
#   return Response(serializer.data,)

# class PageViewSet(viewsets.ModelViewSet):
#   queryset = Page.objects.all()
#   serializer_class = PageSerializer
#   # queryset = Page.objects.all().order_by('-updated')
#   # authentication_classes = [TokenAuthentication, ]
#   # permission_classes = [IsAuthenticated, ]


from rest_framework_mongoengine.generics import *    


@api_view(['GET'])
def getPage(request):
    # serializer_class = PostSerializer
    queryset = Page.objects.all()
    serializer = PostSerializer(queryset,many=True)
    return Response(serializer.data,)

@api_view(['GET'])
def getPageId(request,pk):

  notes = Page.objects.get(id=pk)
  serializer = PostSerializer(notes,many=False)
  return Response(serializer.data)



@api_view(['POST'])
def createPage(request):

  serializer = PostSerializer(data = request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)




@api_view(['PUT'])
def updatePage(request, pk):
  data = request.data
  note = Page.objects.get(id=pk)
  serializer = PostSerializer(instance=note, data=data)
  if serializer.is_valid():
      serializer.save()

  return Response(serializer.data)


@api_view(['DELETE'])
def deletePage(request, pk):
  note = Page.objects.get(id=pk)
  note.delete()
  return Response('Note was deleted!')
