from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serialisers import ToDoListSerializer
from .models import ToDoList


# Create your views here.
def index(response):
    return HttpResponse("<h1> Muskan: My First Webpage Learning </h1>")

def v1(response):
    return HttpResponse("<h1> View 1 ..! </h1>")


@api_view(['GET'])
def getToDoList(request):
    notes = ToDoList.objects.all()
    serializer = ToDoListSerializer(notes, many=True)

    return Response(serializer.data)
