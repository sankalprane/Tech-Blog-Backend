from django.shortcuts import render

# Create your views here.
from .serializers import *
from rest_framework import viewsets
from .models import Blog

class BlogViewSet(viewsets.ModelViewSet):

    serializer_class = BlogSerializer
    queryset = Blog.objects.all()