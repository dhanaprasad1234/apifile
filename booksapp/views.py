from django.shortcuts import render
from .models import Books
from .serializers import bookserializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class Booklist(APIView):
    def get(self,request,format=None):
        book = Books.objects.all()
        serializers = bookserializers(book,many=True)
        return Response(serializers.data)

    def post(self,request,format=None):
        serializers = bookserializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


