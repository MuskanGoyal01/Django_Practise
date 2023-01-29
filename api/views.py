from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializer
from main.models import Item

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "List of all Items": "/api/getData/",
        "View specific Item": "/api/getItem/<str:pk>/",
        "Create a new item": "/api/add/",
        "Update an existing item": "/api/update/<str:pk>/",
        "Delete an item": "/api/delete/<str:pk>/",
        "Generating token": "/api/token",
        "Refreshing token": "/api/token/refresh",
    }

    return Response(api_urls)


@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getItem(request,pk):
    items = Item.objects.get(id=pk)
    serializer = ItemSerializer(items, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateItem(request, pk):
    items = Item.objects.get(id=pk)
    serializer = ItemSerializer(instance=items, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteItem(request, pk):
    items = Item.objects.get(id=pk)
    items.delete()

    return Response("Item successfully deleted.")

